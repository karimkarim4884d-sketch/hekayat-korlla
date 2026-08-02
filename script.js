import { initializeApp } from "https://www.gstatic.com/firebasejs/12.17.0/firebase-app.js";
import { getDatabase, ref, push, set } from "https://www.gstatic.com/firebasejs/12.17.0/firebase-database.js";

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
const db = getDatabase(app);

// تجربة حفظ بيانات
window.saveData = function () {
  let data = {
    name: "تجربة",
    time: new Date().toString()
  };

  const newRef = push(ref(db, "data"));

  set(newRef, data)
    .then(() => {
      alert("تم الحفظ بنجاح");
    })
    .catch((error) => {
      alert("خطأ: " + error.message);
    });
};
