export const INCOME_CATEGORIES = [
  "Salary",
  "Freelance",
  "Business",
  "Investment",
  "Gift",
  "Other",
];

export const EXPENSE_CATEGORIES = [
  "Food",
  "Rent",
  "Transport",
  "Bills",
  "Shopping",
  "Health",
  "Entertainment",
  "Education",
  "Other",
];

export const categoriesFor = (type) =>
  type === "income" ? INCOME_CATEGORIES : EXPENSE_CATEGORIES;
