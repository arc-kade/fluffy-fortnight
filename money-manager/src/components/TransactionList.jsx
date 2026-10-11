import { formatDate, formatMoney } from "../utils/format.js";

const FILTERS = [
  { value: "all", label: "All" },
  { value: "income", label: "Income" },
  { value: "expense", label: "Expenses" },
];

function TransactionList({ transactions, filter, onFilterChange, onDelete }) {
  return (
    <section className="panel">
      <div className="list-header">
        <h2>Transactions</h2>
        <div className="filter-tabs" role="group" aria-label="Filter transactions">
          {FILTERS.map((f) => (
            <button
              key={f.value}
              type="button"
              className={filter === f.value ? "active" : ""}
              aria-pressed={filter === f.value}
              onClick={() => onFilterChange(f.value)}
            >
              {f.label}
            </button>
          ))}
        </div>
      </div>

      {transactions.length === 0 ? (
        <p className="empty">No transactions to show yet.</p>
      ) : (
        <ul className="tx-list">
          {transactions.map((t) => (
            <li key={t.id} className="tx-row">
              <div className="tx-main">
                <span className="tx-title">{t.description || t.category}</span>
                <span className="tx-meta">
                  <span className="tag">{t.category}</span>
                  {formatDate(t.date)}
                </span>
              </div>
              <span className={`tx-amount ${t.type}`}>
                {t.type === "income" ? "+" : "-"}
                {formatMoney(t.amount)}
              </span>
              <button
                type="button"
                className="tx-delete"
                aria-label={`Delete ${t.description || t.category}`}
                onClick={() => onDelete(t.id)}
              >
                ✕
              </button>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}

export default TransactionList;
