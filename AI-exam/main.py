"""
PTMAE — Python Transactional Micro-Banking & Audit Engine
Educational console simulation. Uses only the permitted imports: random, datetime.
"""

import random
import datetime


# ============================================================
# MODULE A — COMMAND INTERFACE, FINANCIAL CALCULATIONS & GUARDS
# ============================================================

SUPPORTED_COMMANDS = {
    "help": "Show available commands",
    "interest": "Calculate compound interest: interest <principal> <annual_rate_percent> <years>",
    "penalty": "Calculate a transaction penalty: penalty <amount> <penalty_rate_percent>",
    "accounts": "Display account records from accounts.db",
    "audit": "Validate records and write audit logs",
    "demo": "Run the finite feature demonstration",
    "exit": "Leave the command console",
}


class BaseSystemError(Exception):
    """Base exception for expected PTMAE system failures."""


class CorruptedRecordError(BaseSystemError):
    """Raised when an account record is malformed or unsupported."""


class OutOfBoundsError(BaseSystemError):
    """Raised when a requested value exceeds an allowed bound."""


class InsufficientBalanceError(BaseSystemError):
    """Raised when a settlement cannot be funded under account policy."""


def compound_interest(principal, annual_rate_percent, years, compounds_per_year=1):
    """Calculate compound interest using repeated multiplication, after validating inputs."""
    # Validate first so invalid values do not enter the iterative calculation.
    if not isinstance(principal, (int, float)) or isinstance(principal, bool) or principal < 0:
        raise ValueError("Principal must be a non-negative number.")
    if not isinstance(annual_rate_percent, (int, float)) or isinstance(annual_rate_percent, bool) or annual_rate_percent < 0:
        raise ValueError("Annual rate must be a non-negative number.")
    if not isinstance(years, int) or isinstance(years, bool) or years < 0:
        raise ValueError("Years must be a non-negative integer.")
    if not isinstance(compounds_per_year, int) or isinstance(compounds_per_year, bool) or compounds_per_year < 1:
        raise ValueError("Compounds per year must be a positive integer.")
    rate_per_period = (annual_rate_percent / 100) / compounds_per_year
    total_periods = years * compounds_per_year
    amount = float(principal)
    period = 0
    while period < total_periods:
        amount = amount * (1 + rate_per_period)
        period += 1
    return amount


def transaction_penalty(amount, penalty_rate_percent, fixed_fee=0.0):
    """Calculate a percentage penalty plus a fixed fee with strict numeric checks."""
    # A single formula makes the assumptions visible and easy to verify.
    for value, label in ((amount, "Amount"), (penalty_rate_percent, "Penalty rate"), (fixed_fee, "Fixed fee")):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError(label + " must be numeric.")
    if amount < 0 or penalty_rate_percent < 0 or fixed_fee < 0:
        raise ValueError("Amount, rate, and fixed fee cannot be negative.")
    return amount * (penalty_rate_percent / 100) + fixed_fee


def guard_trajectory(events, safety_threshold=0.0):
    """Return events inspected and the reason processing stopped."""
    # The loop stops at the first unsafe balance or explicit termination event.
    inspected = []
    reason = "all events processed"
    for event in events:
        inspected.append(event)
        balance = event.get("balance", 0)
        terminate = event.get("terminate", False)
        if balance < safety_threshold or terminate:
            if balance < safety_threshold and terminate:
                reason = "safety threshold and termination event"
            elif balance < safety_threshold:
                reason = "running balance below safety threshold"
            else:
                reason = "termination event"
            break
    return {"inspected": inspected, "reason": reason, "stopped_early": len(inspected) < len(events)}


def run_command_console(scripted_commands=None):
    """Run a nested-loop command interface; scripted commands make demos finite and repeatable."""
    # Script mode consumes a finite sequence; interactive mode keeps prompting until exit.
    script_mode = scripted_commands is not None
    commands = list(scripted_commands) if script_mode else []
    index = 0
    while True:
        while True:
            if script_mode:
                if index >= len(commands):
                    print("Scripted command sequence complete.")
                    return
                raw = commands[index]
                index += 1
                print("ptmae> " + raw)
            else:
                try:
                    raw = input("ptmae> ")
                except (EOFError, KeyboardInterrupt):
                    print("\nConsole closed.")
                    return
            raw = raw.strip()
            if raw == "":
                print("Enter a command or type 'help'.")
                if script_mode:
                    continue
                break
            pieces = raw.split()
            command = pieces[0].lower()
            args = pieces[1:]
            if command == "exit":
                print("Leaving PTMAE console.")
                return
            if command == "help":
                for name, description in SUPPORTED_COMMANDS.items():
                    print("  " + name + " — " + description)
                break
            try:
                if command == "interest":
                    if len(args) not in (3, 4):
                        raise ValueError("Usage: interest <principal> <annual_rate_percent> <years> [compounds_per_year]")
                    value = compound_interest(float(args[0]), float(args[1]), int(args[2]), int(args[3]) if len(args) == 4 else 1)
                    print("Final amount: {:.2f}".format(value))
                elif command == "penalty":
                    if len(args) not in (2, 3):
                        raise ValueError("Usage: penalty <amount> <penalty_rate_percent> [fixed_fee]")
                    value = transaction_penalty(float(args[0]), float(args[1]), float(args[2]) if len(args) == 3 else 0.0)
                    print("Penalty: {:.2f}".format(value))
                elif command == "accounts":
                    records = read_account_records("accounts.db")
                    for number, record in records:
                        print("{}: {}".format(number, record.rstrip("\n")))
                    if not records:
                        print("No records found.")
                elif command == "audit":
                    process_account_file("accounts.db")
                elif command == "demo":
                    print("Use the standalone demonstration at program startup for all feature tests.")
                else:
                    print("Unknown command {!r}. Type 'help' for options.".format(command))
            except (ValueError, OSError, BaseSystemError) as error:
                print("Command error: " + str(error))
            break


# ============================================================
# MODULE B — HANDCRAFTED PARSING & SCOPE DEMONSTRATIONS
# ============================================================

def parse_raw_log_line(line, delimiter=",", quote_char='"'):
    """Parse one delimited line by index, preserving quoted delimiters and empty fields."""
    # Explicit parser states make quote handling visible without split() or replace().
    if not isinstance(line, str) or not isinstance(delimiter, str) or len(delimiter) != 1:
        raise ValueError("Line must be text and delimiter must be one character.")
    if not isinstance(quote_char, str) or len(quote_char) != 1:
        raise ValueError("Quote character must be one character.")
    fields = []
    field_chars = []
    in_quotes = False
    field_was_quoted = False
    index = 0
    while index < len(line):
        char = line[index]
        if char == quote_char:
            if in_quotes:
                if index + 1 < len(line) and line[index + 1] == quote_char:
                    field_chars.append(quote_char)
                    index += 2
                    continue
                in_quotes = False
            elif not field_chars:
                in_quotes = True
                field_was_quoted = True
            else:
                # A quote inside unquoted text is retained literally.
                field_chars.append(char)
        elif char == delimiter and not in_quotes:
            fields.append("".join(field_chars))
            field_chars = []
            field_was_quoted = False
        else:
            field_chars.append(char)
        index += 1
    fields.append("".join(field_chars))
    if in_quotes:
        raise ValueError("Malformed record: quoted field was not closed.")
    return fields


def make_audit_filter(threshold):
    """Return a stateful audit predicate whose counter is private to that closure."""
    # nonlocal updates the enclosing counter without global state or shared counters.
    count = 0

    def audit_filter(event):
        """Count this filter's calls and classify an event against its threshold."""
        nonlocal count
        count += 1
        try:
            value = float(event.get("amount", 0))
        except (AttributeError, TypeError, ValueError):
            return {"accepted": False, "flagged": True, "count": count, "reason": "invalid event"}
        accepted = value <= threshold
        return {
            "accepted": accepted,
            "flagged": not accepted,
            "count": count,
            "reason": "within threshold" if accepted else "amount exceeds threshold",
        }

    def get_count():
        """Expose the closure's count without exposing a mutable counter."""
        return count

    audit_filter.get_count = get_count
    return audit_filter


def build_position_filters(k):
    """Build k positional lambdas that retain their own index via a default argument."""
    # Binding position as a default argument prevents late-binding to the final loop value.
    if not isinstance(k, int) or isinstance(k, bool) or k < 0:
        raise ValueError("k must be a non-negative integer.")
    filters = []
    for position in range(k):
        filters.append(lambda values, position=position: values[position] if position < len(values) else None)
    return filters


# ============================================================
# MODULE C — REVERSE INDEX & IDENTITY-PRESERVING CLEANUP
# ============================================================

def build_service_reverse_index(raw_db):
    """Map each service tag to sorted unique (account, branch) pairs."""
    # A nested-comprehension pipeline creates the service map; set removes duplicate pairs.
    pairs = {
        wanted_service: sorted({
            (account_id, branch_id)
            for branch_id, accounts in raw_db.items()
            for account_id, services in accounts
            for service in services
            if service == wanted_service
        })
        for wanted_service in {
            service
            for accounts in raw_db.values()
            for account_id, services in accounts
            for service in services
        }
    }
    return pairs


def scrub_queue(data_list):
    """Sanitize a heterogeneous list in place while preserving its outer identity."""
    # Work from the original list and delete by index so callers retain the same object.
    if not isinstance(data_list, list):
        raise TypeError("scrub_queue expects a list.")
    index = 0
    while index < len(data_list):
        item = data_list[index]
        if isinstance(item, tuple):
            data_list[index] = list(item)
            item = data_list[index]
        if isinstance(item, set):
            removable = set()
            for value in item:
                if isinstance(value, int) and not isinstance(value, bool) and value % 2 == 0:
                    removable.add(value)
            data_list[index] = item.difference(removable)
            item = data_list[index]
        if isinstance(item, list):
            try:
                item.sort(reverse=True)
            except TypeError:
                # Mixed incomparable values are left in their original order.
                pass
        index += 1

    # Primitive duplicates are deleted by manual index scanning, without a helper collection.
    index = 0
    while index < len(data_list):
        current = data_list[index]
        primitive = current is None or isinstance(current, (str, int, float, bool, bytes))
        if primitive:
            later = index + 1
            duplicate_found = False
            while later < len(data_list):
                candidate = data_list[later]
                candidate_primitive = candidate is None or isinstance(candidate, (str, int, float, bool, bytes))
                if candidate_primitive and type(candidate) is type(current) and candidate == current:
                    del data_list[later]
                    duplicate_found = True
                else:
                    later += 1
            if duplicate_found:
                # Keep the first occurrence; later duplicates were deleted above.
                pass
        index += 1
    return data_list


# ============================================================
# MODULE D — POSITIONAL DATABASE EDITING, LOGS & EXCEPTIONS
# ============================================================

SUPPORTED_ACCOUNT_TYPES = {"SAVINGS", "CURRENT", "CREDIT"}
CHUNK_SIZE = 4096


def validate_account_record(line):
    """Validate an account record and return (account_id, account_type, balance)."""
    # The handcrafted parser ensures record validation follows the same parsing rules.
    fields = parse_raw_log_line(line.rstrip("\r\n"))
    if len(fields) != 3:
        raise CorruptedRecordError("expected exactly 3 fields")
    account_id = fields[0].strip()
    account_type = fields[1].strip().upper()
    if not account_id:
        raise CorruptedRecordError("account ID is empty")
    if account_type not in SUPPORTED_ACCOUNT_TYPES:
        raise CorruptedRecordError("unsupported account type: " + account_type)
    try:
        balance = float(fields[2].strip())
    except ValueError:
        raise CorruptedRecordError("balance is not numeric")
    if balance < 0:
        raise CorruptedRecordError("balance cannot be negative")
    return account_id, account_type, balance


def read_account_records(path):
    """Read records with their one-based line numbers without altering the file."""
    # Sequential reading keeps record numbering accurate and avoids whole-file rewrites.
    records = []
    with open(path, "r", encoding="utf-8", newline="") as handle:
        line_number = 0
        while True:
            line = handle.readline()
            if line == "":
                break
            line_number += 1
            records.append((line_number, line))
    return records


def replace_record_in_place(path, target_account_id, replacement_payload):
    """Replace one line using r+, bounded chunks, seek/tell, and truncate."""
    # For this text-only UTF-8 database, offsets are captured from tell() cookies and
    # the shifting direction is chosen to avoid overwriting unread content.
    if "\n" in replacement_payload or "\r" in replacement_payload:
        raise ValueError("Replacement payload must be one line without newline characters.")
    with open(path, "r+", encoding="utf-8", newline="") as handle:
        record_start = None
        record_end = None
        old_line = None
        line_number = 0
        while True:
            start = handle.tell()
            line = handle.readline()
            if line == "":
                break
            line_number += 1
            try:
                parsed = parse_raw_log_line(line.rstrip("\r\n"))
            except ValueError:
                parsed = []
            if parsed and parsed[0].strip() == target_account_id:
                record_start = start
                record_end = handle.tell()
                old_line = line
                break
        if record_start is None:
            raise OutOfBoundsError("Account not found: " + target_account_id)

        old_content = old_line.rstrip("\r\n")
        old_ending = ""
        if old_line.endswith("\r\n"):
            old_ending = "\r\n"
        elif old_line.endswith("\n"):
            old_ending = "\n"
        elif old_line.endswith("\r"):
            old_ending = "\r"
        new_text = replacement_payload + old_ending
        old_length = record_end - record_start
        new_length = len(new_text)
        delta = new_length - old_length

        # Move the tail backward for expansion and forward for contraction, in bounded chunks.
        handle.seek(0, 2)
        file_end = handle.tell()
        tail_start = record_end
        tail_length = file_end - tail_start
        if delta > 0:
            remaining = tail_length
            while remaining > 0:
                chunk_length = CHUNK_SIZE if remaining > CHUNK_SIZE else remaining
                source_position = tail_start + remaining - chunk_length
                handle.seek(source_position)
                chunk = handle.read(chunk_length)
                handle.seek(source_position + delta)
                handle.write(chunk)
                remaining -= chunk_length
        elif delta < 0:
            moved = 0
            while moved < tail_length:
                chunk_length = CHUNK_SIZE if tail_length - moved > CHUNK_SIZE else tail_length - moved
                source_position = tail_start + moved
                handle.seek(source_position)
                chunk = handle.read(chunk_length)
                handle.seek(source_position + delta)
                handle.write(chunk)
                moved += chunk_length

        handle.seek(record_start)
        handle.write(new_text)
        handle.truncate(file_end + delta)
        return {"line_number": line_number, "old_record": old_content, "new_record": replacement_payload}


def append_audit(path, message):
    """Append a timestamped message to an audit destination."""
    # The timestamp format is stable and readable for manual inspection.
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    with open(path, "a", encoding="utf-8", newline="") as handle:
        handle.write(timestamp + " | " + message + "\n")


def process_account_file(path, replacement_account=None, replacement_payload=None):
    """Validate each row, log accepted rows and rejections, and always report totals."""
    # Per-record finally reports cleanup; outer finally always prints aggregate counts.
    processed = 0
    rejected = 0
    try:
        records = read_account_records(path)
        for line_number, line in records:
            processed += 1
            try:
                account_id, account_type, balance = validate_account_record(line)
                if replacement_account == account_id and replacement_payload is not None:
                    result = replace_record_in_place(path, account_id, replacement_payload)
                    append_audit("ledger.txt", "Updated line {}: {} -> {}".format(
                        result["line_number"], result["old_record"], result["new_record"]))
                else:
                    append_audit("ledger.txt", "Accepted line {}: {} ({}, {:.2f})".format(
                        line_number, account_id, account_type, balance))
            except (CorruptedRecordError, OutOfBoundsError, ValueError, OSError) as error:
                rejected += 1
                with open("corrupted.log", "a", encoding="utf-8", newline="") as handle:
                    handle.write("line {} | {} | {}\n".format(line_number, str(error), line.rstrip("\r\n")))
            else:
                pass
            finally:
                print("Record {} processed.".format(line_number))
    finally:
        print("Account-file run summary: processed={}, rejected={}".format(processed, rejected))
    return {"processed": processed, "rejected": rejected}


# ============================================================
# MODULE E — ENCAPSULATION, INHERITANCE & BATCH SETTLEMENT
# ============================================================

class Account:
    """Base account with validated private balance and shared account counter."""

    total_accounts = 0

    def __init__(self, account_id, balance):
        """Initialize an account after validating its identifier and opening balance."""
        # Store balance privately and use the public setter to enforce the invariant.
        if not isinstance(account_id, str) or not account_id.strip():
            raise ValueError("Account ID must be a non-empty string.")
        self._account_id = account_id
        self.__balance = 0.0
        self.balance = balance
        Account.total_accounts += 1

    @property
    def balance(self):
        """Return the validated balance through a getter."""
        return self.__balance

    @balance.setter
    def balance(self, value):
        """Set the balance only when it is a finite non-negative numeric value."""
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError("Balance must be numeric.")
        if value < 0 or value != value or value == float("inf") or value == float("-inf"):
            raise ValueError("Balance must be finite and non-negative.")
        self.__balance = float(value)

    def _change_balance(self, new_balance):
        """Update private storage through the validated property."""
        self.balance = new_balance

    def process_settlement(self, amount):
        """Base settlement implementation; subclasses provide account-specific policy."""
        raise NotImplementedError("Subclasses must implement process_settlement().")

    @staticmethod
    def validate_amount(amount):
        """Reject non-positive, non-numeric, and non-finite settlement amounts."""
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError("Settlement amount must be numeric.")
        if amount <= 0 or amount != amount or amount == float("inf") or amount == float("-inf"):
            raise ValueError("Settlement amount must be finite and greater than zero.")


class SavingsAccount(Account):
    """Savings account that protects a minimum closing balance of 1000."""

    def __init__(self, account_id, balance):
        """Initialize savings state through the base constructor."""
        # super() ensures common identity and balance validation is never bypassed.
        super().__init__(account_id, balance)

    def process_settlement(self, amount):
        """Debit a settlement only when at least 1000 remains."""
        self.validate_amount(amount)
        new_balance = self.balance - amount
        if new_balance < 1000:
            raise InsufficientBalanceError("Savings settlement would leave less than 1000.")
        self._change_balance(new_balance)
        return "Savings {} settled; balance {:.2f}".format(self._account_id, self.balance)


class CurrentAccount(Account):
    """Current account with a private overdraft limit."""

    def __init__(self, account_id, balance, overdraft_limit=2000.0):
        """Initialize a current account and validate its overdraft policy."""
        # The parent validates common account state; this class validates its own limit.
        super().__init__(account_id, balance)
        if not isinstance(overdraft_limit, (int, float)) or isinstance(overdraft_limit, bool) or overdraft_limit < 0:
            raise ValueError("Overdraft limit must be a non-negative number.")
        self.__overdraft_limit = float(overdraft_limit)

    def process_settlement(self, amount):
        """Debit only when the resulting balance stays above the negative overdraft limit."""
        self.validate_amount(amount)
        new_balance = self.balance - amount
        if new_balance < -self.__overdraft_limit:
            raise OutOfBoundsError("Settlement exceeds current-account overdraft limit.")
        # The check above happens before balance mutation.
        self._change_balance(new_balance)
        return "Current {} settled; balance {:.2f}".format(self._account_id, self.balance)


class CreditAccount(Account):
    """Credit account that charges a 2.5 percent surcharge on each settlement."""

    def __init__(self, account_id, available_credit):
        """Initialize available credit through the parent balance field."""
        # For this educational model, balance represents remaining available credit.
        super().__init__(account_id, available_credit)

    def process_settlement(self, amount):
        """Deduct amount plus the explicit 2.5 percent surcharge from available credit."""
        self.validate_amount(amount)
        surcharge = amount * 2.5 / 100
        final_debit = amount + surcharge
        if final_debit > self.balance:
            raise InsufficientBalanceError("Settlement plus surcharge exceeds available credit.")
        self._change_balance(self.balance - final_debit)
        return "Credit {} settled (debit {:.2f}); available {:.2f}".format(
            self._account_id, final_debit, self.balance)


def run_batch(accounts, amount):
    """Run a polymorphic settlement for every account and isolate per-account failures."""
    # Each exception is caught inside the loop so later accounts always get a chance.
    succeeded = 0
    failed = 0
    for account in accounts:
        try:
            print(account.process_settlement(amount))
            succeeded += 1
        except (BaseSystemError, ValueError, TypeError) as error:
            failed += 1
            print("Settlement failed for {}: {}".format(getattr(account, "_account_id", "unknown"), error))
    print("Batch summary: successful={}, failed={}".format(succeeded, failed))
    return {"successful": succeeded, "failed": failed}


# ============================================================
# DEMONSTRATION FIXTURES AND SELF-CHECKS
# ============================================================

def create_demo_database(path):
    """Create a new demo database only if the destination does not already exist."""
    # Exclusive creation protects an existing user file from accidental overwrite.
    try:
        with open(path, "x", encoding="utf-8", newline="") as handle:
            handle.write("Acc101,SAVINGS,5200.00\n")
            handle.write("Acc102,CURRENT,1500.00\n")
            handle.write("Acc103,UNKNOWN,700.00\n")
            handle.write("Acc104,SAVINGS,not-a-number\n")
            handle.write("Acc105,CREDIT,900.00")
        return True
    except FileExistsError:
        print("{} already exists; leaving it untouched.".format(path))
        return False


def run_feature_demonstration():
    """Exercise required features using safe demo fixtures and print observable results."""
    # A finite scripted console and uniquely named demo file keep the demonstration repeatable.
    print("\n=== PTMAE FEATURE DEMONSTRATION ===")
    run_command_console(["help", "interest 1000 5 2", "penalty 200 2.5 1", "unknown", "exit"])

    print("\n[A] Calculators and trajectory guard")
    print("Compound amount:", round(compound_interest(1000, 5, 2), 2))
    print("Penalty:", round(transaction_penalty(200, 2.5, 1), 2))
    print("Threshold stop:", guard_trajectory([
        {"balance": 500, "terminate": False}, {"balance": -1, "terminate": False},
        {"balance": 50, "terminate": False}], safety_threshold=0))
    print("Termination stop:", guard_trajectory([
        {"balance": 500, "terminate": False}, {"balance": 400, "terminate": True},
        {"balance": 300, "terminate": False}], safety_threshold=0))

    print("\n[B] Parser cases")
    parser_cases = [
        "Acc101,SAVINGS,5200.00",
        'Acc102,"CURRENT, PREMIUM",1500.00',
        '"Acc""103",SAVINGS,10.00',
        "A,,10",
        "A,SAVINGS,",
        '"unfinished,SAVINGS,1',
    ]
    for sample in parser_cases:
        try:
            print(repr(sample), "=>", parse_raw_log_line(sample))
        except ValueError as error:
            print(repr(sample), "=> expected parser error:", error)

    print("\n[B] Independent closures and positional lambdas")
    low_filter = make_audit_filter(100)
    high_filter = make_audit_filter(500)
    print("Low filter:", low_filter({"amount": 120}), "count:", low_filter.get_count())
    print("High filter:", high_filter({"amount": 120}), "count:", high_filter.get_count())
    print("Low filter second call:", low_filter({"amount": 50}), "count:", low_filter.get_count())
    sample_values = ["zero", "one", "two"]
    print("Lambda outputs:", [function(sample_values) for function in build_position_filters(3)])

    print("\n[C] Reverse index and queue cleanup")
    raw_db = {
        "BRANCH_01": [("Acc1@1", {"DEPOSIT", "UPI"}), ("Acc1@2", {"LOAN", "UPI"})],
        "BRANCH_02": [("Acc101", {"SAVINGS", "UPI"}), ("Acc103", {"CARD", "DEPOSIT"})],
    }
    reverse_index = build_service_reverse_index(raw_db)
    print("Reverse index:", reverse_index)
    print("UPI pairs:", reverse_index["UPI"])
    queue = [(3, 1), [2, 9, 4], {2, 3, 4, 5}, 7, 7, "x", "x", None]
    original_id = id(queue)
    scrub_queue(queue)
    print("Sanitized queue:", queue)
    print("Outer list identity preserved:", original_id == id(queue), "id:", original_id)

    print("\n[D] Safe demo database, record validation, and positional edit")
    demo_path = "ptmae_demo_accounts.db"
    created = create_demo_database(demo_path)
    if created:
        process_account_file(demo_path)
        before = read_account_records(demo_path)
        print("Before update:", [line.rstrip("\n") for number, line in before])
        update = replace_record_in_place(demo_path, "Acc101", "Acc101,SAVINGS,8750.00")
        print("Different-length update:", update)
        after = read_account_records(demo_path)
        print("After update:", [line.rstrip("\n") for number, line in after])
        print("Neighbour records preserved:", len(before) == len(after) and before[1:] == after[1:])
        append_audit("ledger.txt", "Demonstration updated " + update["new_record"])
    else:
        print("Skipped fixture-dependent file surgery to avoid modifying existing data.")
        print("Delete ptmae_demo_accounts.db manually only if it is a disposable demo file.")
    print("Audit destinations: ledger.txt and corrupted.log (append-only).")

    print("\n[E] Accounts, name mangling, and resilient batch")
    savings = SavingsAccount("SAV-1", 3000)
    current = CurrentAccount("CUR-1", 1000, 500)
    credit = CreditAccount("CRD-1", 1000)
    print(savings.process_settlement(500))
    try:
        savings.process_settlement(2000)
    except InsufficientBalanceError as error:
        print("Expected savings failure:", error)
    print(current.process_settlement(1200))
    try:
        current.process_settlement(1000)
    except OutOfBoundsError as error:
        print("Expected current failure:", error)
    print(credit.process_settlement(100))
    try:
        credit.process_settlement(1000)
    except InsufficientBalanceError as error:
        print("Expected credit failure:", error)
    print("Mangled balance:", savings._Account__balance)
    try:
        print(savings.__balance)
    except AttributeError as error:
        print("Direct __balance access fails as expected:", type(error).__name__)
    print("Total accounts:", Account.total_accounts)
    print("Batch (one failure, later account continues):")
    run_batch([SavingsAccount("BATCH-1", 5000), SavingsAccount("BATCH-2", 1200),
               CurrentAccount("BATCH-3", 100, 500), CreditAccount("BATCH-4", 1000)], 500)
    print("\n=== DEMONSTRATION COMPLETE ===")


def main():
    """Select a finite educational demonstration or launch the interactive console."""
    # The default runs a repeatable demonstration; --interactive starts the persistent CLI.
    try:
        choice = input("PTMAE: enter D for demo or I for interactive console [D]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        choice = "d"
    if choice == "i":
        run_command_console()
    else:
        run_feature_demonstration()


if __name__ == "__main__":
    main()
