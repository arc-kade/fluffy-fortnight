// All localStorage access lives here so pages and components never touch
// raw keys or JSON parsing.

const USERS_KEY = "mm_users";
const SESSION_KEY = "mm_currentUser";
const transactionsKey = (userKey) => `mm_transactions:${userKey}`;

function read(key, fallback) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : fallback;
  } catch {
    return fallback;
  }
}

function write(key, value) {
  localStorage.setItem(key, JSON.stringify(value));
}

// "Alice " and "alice" are the same account
export const normalizeUsername = (name) => name.trim().toLowerCase();

export function getUsers() {
  const users = read(USERS_KEY, {});
  return users && typeof users === "object" && !Array.isArray(users) ? users : {};
}

export function registerUser(username, password) {
  const key = normalizeUsername(username);
  const users = getUsers();

  if (users[key]) {
    return { ok: false, error: "That username is already taken" };
  }

  users[key] = {
    displayName: username.trim(),
    password, // plain text: fine for a learning project, never for a real app
    createdAt: new Date().toISOString(),
  };
  write(USERS_KEY, users);
  return { ok: true };
}

export function loginUser(username, password) {
  const key = normalizeUsername(username);
  const user = getUsers()[key];

  if (!user || user.password !== password) {
    return { ok: false, error: "Invalid username or password" };
  }

  localStorage.setItem(SESSION_KEY, key);
  return { ok: true };
}

export function getCurrentUser() {
  const key = localStorage.getItem(SESSION_KEY);
  if (!key) return null;
  const user = getUsers()[key];
  return user ? { key, displayName: user.displayName } : null;
}

export function logoutUser() {
  // Only the session is cleared; the user's transactions stay saved
  localStorage.removeItem(SESSION_KEY);
}

export function loadTransactions(userKey) {
  const list = read(transactionsKey(userKey), []);
  return Array.isArray(list) ? list : [];
}

export function saveTransactions(userKey, list) {
  write(transactionsKey(userKey), list);
}
