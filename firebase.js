import { initializeApp } from "https://www.gstatic.com/firebasejs/12.17.0/firebase-app.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/12.17.0/firebase-database.js";

const firebaseConfig = {
  apiKey: "AIzaSyCfAqlHPGsdZ0c0Ndwrl2YfSuu2Z48FjDI",
  authDomain: "zack-cinema.firebaseapp.com",
  databaseURL: "https://zack-cinema-default-rtdb.firebaseio.com",
  projectId: "zack-cinema",
  storageBucket: "zack-cinema.firebasestorage.app",
  messagingSenderId: "166273951321",
  appId: "1:166273951321:web:1472ff55831ade6b087348"
};

const app = initializeApp(firebaseConfig);

export const db = getDatabase(app);
