import { formatMoney } from "../utils/format.js";

function SummaryCards({ income, expenses }) {
  const balance = income - expenses;

  return (
    <section className="summary" aria-label="Summary">
      <div className="summary-card">
        <span className="summary-label">Balance</span>
        <span
          className={`summary-value ${balance < 0 ? "negative" : ""}`}
          data-testid="balance"
        >
          {formatMoney(balance)}
        </span>
      </div>
      <div className="summary-card income">
        <span className="summary-label">Total income</span>
        <span className="summary-value" data-testid="total-income">
          {formatMoney(income)}
        </span>
      </div>
      <div className="summary-card expense">
        <span className="summary-label">Total expenses</span>
        <span className="summary-value" data-testid="total-expenses">
          {formatMoney(expenses)}
        </span>
      </div>
    </section>
  );
}

export default SummaryCards;
