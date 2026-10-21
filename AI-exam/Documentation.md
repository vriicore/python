# PTMAE --- Python Transactional Micro-Banking & Audit Engine

## 1. Project overview

PTMAE is a console-based **educational banking simulation**. It
demonstrates validated account objects, settlement policies, custom
exceptions, manual delimited-record parsing, closure state with
`nonlocal`, lambda capture, reverse indexing, in-place list cleanup,
append-only audit logs, and positional file editing.

It is not a real banking system. It does not connect to financial
institutions, authenticate users, encrypt records, provide
concurrent-write protection, or meet regulatory requirements. The
database and logs are plain-text teaching fixtures.

### Learning outcomes

-   Write focused functions and classes with docstrings and explanatory
    comments.
-   Validate user input and handle recoverable exceptions.
-   Demonstrate inheritance, encapsulation, name mangling, and
    polymorphism.
-   Parse delimited records without using `str.split()` or
    `str.replace()` in the parser.
-   Use `nonlocal` to maintain independent closure state.
-   Preserve list identity while cleaning mutable data.
-   Edit an existing line in `r+` mode using `tell()`, `seek()`, bounded
    chunks, and `truncate()`.
-   Distinguish accepted and rejected records with audit destinations.

## 2. Architecture

``` text
                         +-----------------------+
                         | Console / main()      |
                         | help, interest, exit   |
                         +-----------+-----------+
                                     |
                +--------------------+--------------------+
                |                    |                    |
      +---------v---------+  +-------v--------+  +--------v---------+
      | Financial tools   |  | Parser + audit |  | Data utilities   |
      | compound interest |  | parser, filters|  | reverse index    |
      | transaction fee   |  | lambda capture |  | queue sanitizing |
      +-------------------+  +-------+--------+  +------------------+
                                     |
                         +-----------v-----------+
                         | Record validation     |
                         | accounts.db / r+ edit |
                         | ledger.txt / log      |
                         +-----------+-----------+
                                     |
                         +-----------v-----------+
                         | Custom exception tree |
                         | BaseSystemError       |
                         +-----------------------+

       +---------------------+       +---------------------------+
       | Account              |       | run_batch(accounts, amt)  |
       | private __balance    +------>| polymorphic coordinator   |
       | validated property   |       +-------------+-------------+
       +----------+-----------+                     |
                  |                                 |
       +----------+-----------+---------------------+
       |                      |                     |
+------v-------+      +-------v--------+     +------v-------+
| Savings      |      | Current        |     | Credit       |
| min balance  |      | overdraft cap  |     | 2.5% fee     |
+--------------+      +----------------+     +--------------+
```

## 3. Files and generated outputs

-   `main.py` --- executable source.
-   `Documentation.md` --- this report.
-   `ptmae_demo_accounts.db` --- created by the demonstration only if it
    does not already exist.
-   `ledger.txt` --- timestamped accepted/update events; appended to.
-   `corrupted.log` --- rejected record details and line numbers;
    appended to.

The demo fixture uses exclusive `x` creation. If
`ptmae_demo_accounts.db` already exists, the program leaves it untouched
and skips fixture-dependent editing. The audit files are append-only, so
repeated runs add entries rather than silently erasing previous history.

## 4. Requirements and implementation notes

### Module A --- CLI, calculations, and trajectory guard

-   `run_command_console()` uses nested loops and supports `help`,
    `interest`, `penalty`, `accounts`, `audit`, `demo`, and `exit`.
-   The CLI catches expected input, I/O, and domain exceptions and
    continues.
-   `compound_interest()` uses repeated multiplication. Formula:
    (A=P(1+r/n)\^{nt}), where `r` is the annual rate as a decimal, `n`
    is compounding periods per year, and `t` is whole years. The
    function returns the final amount, not only the interest earned.
-   `transaction_penalty()` uses `amount × rate/100 + fixed_fee`.
-   `guard_trajectory()` returns the events inspected and a reason. It
    stops at the first balance below the threshold or event with
    `terminate=True`; the combined condition uses short-circuit logic.

### Module B --- parser and scope

`parse_raw_log_line(line, delimiter=",", quote_char='"')` walks the
string with an index and tracks quoted state. Delimiters inside quoted
fields are data; two adjacent quote characters inside a quoted field
represent one literal quote. Adjacent delimiters and a trailing
delimiter produce empty fields. An unclosed quote raises `ValueError`
rather than silently accepting a malformed record. The parser does not
call `split()` or `replace()`.

`make_audit_filter(threshold)` returns a callable with an independent
counter. Its inner function increments that counter through `nonlocal`.
`get_count()` reads the count. `build_position_filters(k)` captures each
position in a default parameter (`position=position`), avoiding
late-binding.

### Module C --- reverse index and queue cleanup

`build_service_reverse_index()` uses a nested-comprehension pipeline to
collect each service's unique `(account_id, branch_id)` pairs and sorts
them. In the supplied data, `UPI` maps to: - `("Acc101", "BRANCH_02")` -
`("Acc1@1", "BRANCH_01")` - `("Acc1@2", "BRANCH_01")`

A reverse index makes service-based lookups direct: the caller can
retrieve all accounts offering a service without scanning every branch
each time.

`scrub_queue()` modifies the outer list in place, converts tuples to
lists, removes even integers from sets using set difference, sorts
sortable nested lists in descending order, and manually deletes
duplicate primitive values by index. Mixed incomparable nested lists are
left unsorted instead of causing the operation to fail. The function
preserves `id(data_list)`.

### Module D --- record validation, file surgery, and logs

The supported record format is `Account_ID,TYPE,BALANCE`, for example
`Acc101,SAVINGS,5200.00`. Types are `SAVINGS`, `CURRENT`, and `CREDIT`.
A wrong field count, empty ID, unsupported type, nonnumeric balance, or
negative balance is rejected.

`replace_record_in_place()` opens the existing file with `r+`, finds the
target by sequential reading, remembers the record boundaries with
`tell()`, and moves the tail in bounded chunks. It shifts the tail
backward for a longer replacement and forward for a shorter replacement,
writes the new record, then truncates to the adjusted end. The original
line ending is preserved, including the no-newline final-record case.

**Text-stream limitation:** text-mode `tell()` values are opaque seek
cookies, not universally interchangeable with byte offsets or arbitrary
character counts. The implementation is intended for the supported
simple UTF-8, line-oriented database format and uses positions obtained
from the same open text stream. For a production-grade
arbitrary-encoding editor, a binary format with explicitly defined byte
offsets and encoding boundaries would be preferable.

For each input record, `process_account_file()` visibly uses `try`,
`except`, `else`, and `finally` flow. Rejections are written to
`corrupted.log` with their original line number; accepted records and
successful updates are written to `ledger.txt` with timestamps. The
per-record `finally` prints a status, while the outer `finally` prints
aggregate totals.

**Important behaviour:** `process_account_file()` reads the record list
before processing. If a requested replacement is used, the line content
changes on disk while the loop's original record snapshot remains the
basis for that pass. The demo performs the edit separately after
validation so this distinction is visible.

### Module E --- accounts and batch settlement

-   `Account` stores balance in `__balance` and exposes it through the
    validated `balance` property. `_account_id` is a
    protected-by-convention identifier.
-   `SavingsAccount` refuses a debit that would leave less than 1000.
-   `CurrentAccount` allows a negative balance only down to its private
    overdraft limit. It checks the limit before mutation.
-   `CreditAccount` charges a 2.5% surcharge and debits the final amount
    from available credit.
-   Every subclass initializes its parent with `super().__init__()`.
-   `run_batch()` catches each account's failure inside the loop and
    continues with later accounts.

Python name mangling changes `__balance` in `Account` to
`_Account__balance`. An external expression such as `account.__balance`
ordinarily raises `AttributeError`, while `account._Account__balance`
can access the attribute. Name mangling helps avoid accidental
collisions; it is not a security boundary.

## 5. Scope and state visibility

  ----------------------------------------------------------------------------------------------------------------------
  State kind                Where it is stored                           Access method              Intended modifier
  ------------------------- -------------------------------------------- -------------------------- --------------------
  Module-level constants    Module namespace,                            Referenced by functions    Defined once during
                            e.g. `SUPPORTED_ACCOUNT_TYPES`                                          startup

  Class attribute           `Account.total_accounts`                     `Account.total_accounts`   `Account.__init__`
                                                                                                    increments it

  Enclosing-scope variable  Closure cell for `count`                     Inner filter; read through Inner filter using
                                                                         `get_count()`              `nonlocal`

  Instance                  `account._account_id`                        Direct internal use by     Constructor
  protected-by-convention                                                account classes            
  field                                                                                             

  Private base balance      `account._Account__balance` after name       Public `balance` property  Validated property
                            mangling                                     is intended API            setter

  Private subclass limit    `current._CurrentAccount__overdraft_limit`   Internal `CurrentAccount`  Constructor
                            after mangling                               methods                    
  ----------------------------------------------------------------------------------------------------------------------

"Protected" and "private" are naming conventions/mechanisms in Python,
not access-control security.

## 6. Requirements traceability and compliance matrix

The provided brief defines engineering constraints C-01 through C-09 and
functional modules A through E, but it does **not** include the official
definitions for the requested `FR-*`, `NFR-*`, or Unit 1--5 syllabus
identifiers. Therefore, official traceability for those identifiers is
pending. The table below maps the brief's concrete requirements; it does
not claim to be the institution's official FR/NFR matrix.

  ---------------------------------------------------------------------------------------------------------------------
  Requirement ID     Requirement            Implementation location         Documentation   Verification    Status
                     description                                            location        method          
  ------------------ ---------------------- ------------------------------- --------------- --------------- -----------
  C-01               Only `random` and      Imports at top of `main.py`     This section    Inspect import  Pass
                     `datetime` imports                                                     lines           

  C-02               Character-index        `parse_raw_log_line`            Module B        Search function Pass
                     parser; no parser                                                      body and run    
                     `split`/`replace`                                                      parser cases    

  C-03               Manual loops instead   Financial and collection        Modules A/C     Inspect source  Pass
                     of unnecessary         functions                                                       
                     `max/min/sum`                                                                          

  C-04               Closure counter uses   `make_audit_filter`             Module B        Run two filters Pass
                     `nonlocal`; no                                                         independently   
                     `global`                                                                               

  C-05               In-place list mutation `scrub_queue`                   Module C        Compare `id()`  Pass
                     preserves identity                                                     before/after    

  C-06               Existing database      `replace_record_in_place`       Module D        Inspect open    Pass
                     edits use `r+` and                                                     mode and file   
                     positional operations                                                  operations      

  C-07               File handles are       All file functions use `with`   Modules         Inspect         Pass
                     managed safely                                         D/Execution     file-opening    
                                                                                            sites           

  C-08               Subclass constructors  Three subclasses                Module E        Inspect         Pass
                     call                                                                   constructors    
                     `super().__init__()`                                                                   

  C-09               Private balance,       `Account`, demo                 Module E        Run attribute   Pass
                     validated access, name                                                 access          
                     mangling demonstration                                                 demonstration   

  A.1                Interactive console    `run_command_console`, `main`   Module A        Run `I` and `D` Pass
                     and scripted mode                                                      modes           

  A.2                Compound interest and  `compound_interest`,            Module A        Compare sample  Pass
                     penalty calculator     `transaction_penalty`                           calculations    

  A.3                Guard stops on low     `guard_trajectory`              Module A        Run both demo   Pass
                     balance or termination                                                 trajectories    

  B.1                Manual quoted-field    `parse_raw_log_line`            Module B        Six parser      Pass
                     parser and edge cases                                                  examples        

  B.2                Independent stateful   `make_audit_filter`             Module B        Compare         Pass
                     audit closures                                                         counters        

  B.3                Positional lambda      `build_position_filters`        Module B        Apply all       Pass
                     capture                                                                lambdas to      
                                                                                            sample list     

  C.1                Sorted unique reverse  `build_service_reverse_index`   Module C        Inspect UPI     Pass
                     index                                                                  mapping         

  C.2                In-place heterogeneous `scrub_queue`                   Module C        Check contents  Pass
                     queue cleanup                                                          and identity    

  D.1                Custom exception       Exception declarations          Module D        Import/run      Pass
                     hierarchy                                                              exception cases 

  D.2                Validate records using `validate_account_record`       Module D        Test valid and  Pass
                     handcrafted parser                                                     corrupt records 

  D.3                Length-changing `r+`   `replace_record_in_place`       Module D        Compare         Pass
                     record edit                                                            neighbouring    
                                                                                            rows            

  D.4                Dual logs and          `append_audit`,                 Module D        Inspect logs    Pass
                     exception-flow         `process_account_file`                          and printed     
                     accounting                                                             counts          

  E.1                Encapsulated base      `Account`                       Module E        Run attribute   Pass
                     account and mangling                                                   access test     

  E.2                Three account policies Account subclasses              Module E        Success and     Pass
                     and parent                                                             failure         
                     initialization                                                         settlements     

  E.3                Polymorphic resilient  `run_batch`                     Module E        Confirm later   Pass
                     batch                                                                  accounts run    
                                                                                            after failure   

  FR-1.1--FR-1.3     Official descriptions  Pending mapping                 This section    Compare with    Not
                     not present in                                                         official        Verified
                     supplied brief                                                         assignment      

  FR-2.1--FR-2.3     Official descriptions  Pending mapping                 This section    Compare with    Not
                     not present in                                                         official        Verified
                     supplied brief                                                         assignment      

  FR-3.1--FR-3.2.4   Official descriptions  Pending mapping                 This section    Compare with    Not
                     not present in                                                         official        Verified
                     supplied brief                                                         assignment      

  FR-4.1--FR-4.3.3   Official descriptions  Pending mapping                 This section    Compare with    Not
                     not present in                                                         official        Verified
                     supplied brief                                                         assignment      

  FR-5.1.1--FR-5.3   Official descriptions  Pending mapping                 This section    Compare with    Not
                     not present in                                                         official        Verified
                     supplied brief                                                         assignment      

  All applicable     Official NFR list not  Provisional coverage:           This section    Compare with    Not
  NFRs               present in supplied    C-01--C-09 and code-quality                     official        Verified
                     brief                  standards                                       assignment      

  Unit 1--5 syllabus Syllabus topic list    Relevant topics are mapped in   This section    Compare with    Not
  topics             not present in         Modules A--E                                    official        Verified
                     supplied brief                                                         syllabus        
  ---------------------------------------------------------------------------------------------------------------------

### Why some rows are not verified

The project brief explicitly instructs that official FR/NFR descriptions
and syllabus topics must not be invented. Supply the official assignment
specification and Unit 1--5 syllabus to replace the pending rows with
exact wording and verified source-to-code mappings.

## 7. Test plan and expected results

  ------------------------------------------------------------------------------------
  Test                    Input / action                       Expected result
  ----------------------- ------------------------------------ -----------------------
  Compound interest       `compound_interest(1000, 5, 2)`      Approximately `1102.50`

  Penalty                 `transaction_penalty(200, 2.5, 1)`   `6.0`

  Invalid rate            Negative annual rate                 `ValueError`

  Low-balance guard       First event balance below threshold  Stops at that event

  Termination guard       Event with `terminate=True`          Stops at that event

  Quoted delimiter        `A,"CURRENT, PREMIUM",10`            Three fields; middle
                                                               field retains comma

  Escaped quote           `"Acc""103",SAVINGS,10`              First field is
                                                               `Acc"103`

  Empty values            `A,,10` and `A,SAVINGS,`             Empty field preserved

  Incomplete quote        `"unfinished,SAVINGS,1`              `ValueError`

  Independent closures    Call low and high filters            Each count changes
                                                               independently

  Lambda capture          Three positional lambdas             Returns `zero`, `one`,
                                                               `two`

  Reverse index           Supplied `raw_db`                    UPI has three
                                                               account/branch pairs

  Queue identity          Save `id(queue)`, scrub, compare     Identity unchanged

  Corrupt record          Unsupported type / nonnumeric        Logged in
                          balance                              `corrupted.log` with
                                                               line number

  Longer replacement      Replace `5200.00` with `8750.00`     Target line changes;
                                                               following rows
                                                               preserved

  Savings boundary        Debit leaving exactly 1000           Accepted; below 1000
                                                               rejected

  Current overdraft       Debit beyond negative limit          `OutOfBoundsError`,
                                                               balance unchanged

  Credit surcharge        Debit 100                            Total credit debit is
                                                               102.50

  Batch isolation         One failing account before another   Later accounts still
                          account                              processed
  ------------------------------------------------------------------------------------

The startup demonstration prints observable outputs for these examples.
These are expected behaviours, not a claim that an external test suite
has been run.

## 8. Execution and maintenance guide

### Run

``` bash
python main.py
```

At startup, enter `D` (or press Enter) for the finite demonstration, or
`I` for the interactive console.

### CLI examples

``` text
help
interest 1000 5 2
interest 1000 5 2 4
penalty 200 2.5
penalty 200 2.5 1
accounts
audit
exit
```

The interactive commands use whitespace-separated arguments. Do not
enter thousands separators in numeric amounts.

### Log interpretation

-   `ledger.txt`: timestamped accepted record and update descriptions.
-   `corrupted.log`: original line number, rejection reason, and source
    line.
-   The two audit files are appended to; the program does not clear them
    automatically.

### Safe reset

1.  Exit the program.
2.  Confirm that `ptmae_demo_accounts.db` is only a disposable
    demonstration fixture.
3.  Back up any file you need.
4.  Delete the demo fixture manually if you want it recreated on the
    next run.
5.  Delete or archive `ledger.txt` and `corrupted.log` only if you
    intentionally want to reset the audit history.
6.  Never point the demonstration at a real or valuable database file.

### Common errors

-   `Account not found`: the target ID is not present in the database.
-   `Malformed record`: a quoted field was not closed.
-   `unsupported account type`: the type is not one of `SAVINGS`,
    `CURRENT`, or `CREDIT`.
-   `already exists`: safe demo fixture creation declined to overwrite
    an existing file.
-   A settlement exception indicates the account's policy would be
    violated; the balance should remain unchanged for that failed
    operation.

## 9. Assumptions and limitations

1.  The official FR/NFR wording and Unit 1--5 syllabus were not included
    in the provided project brief, so their exact traceability remains
    unverified.
2.  The database is a simple line-oriented text file with
    comma-delimited fields and supported UTF-8 text.
3.  Record replacement preserves the target line's existing line ending.
    A final record without a newline remains without a newline.
4.  `CreditAccount` models its `balance` as remaining available credit,
    rather than a conventional positive debt balance.
5.  `CurrentAccount` permits a negative balance up to its configured
    overdraft limit.
6.  `SavingsAccount` enforces a minimum remaining balance of 1000.
7.  The audit logs are append-only and are not rotated or protected
    against tampering.
8.  This is an educational single-process demonstration, not production
    financial software.
