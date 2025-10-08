# 🧠 Notification System – Advanced OOP (Inheritance + Polymorphism + Composition)

## 🔹 Overview
This project demonstrates **advanced Object-Oriented Programming (OOP)** concepts using Python.  
It builds a clean and modular **Notification System** that sends messages through multiple channels such as Email, SMS, WhatsApp, and Push Notifications — all built using **inheritance**, **polymorphism**, and **composition**.

---

## ⚙️ Features
- **Abstract Base Class (`Notification`)** enforcing structure through `abc` module.  
- **Four Subclasses:**
  - `EmailNotification` ✉️  
  - `SMSNotification` 📱  
  - `WhatsappNotification` 💬  
  - `PushNotification` 🔔  
- **Polymorphism:** Each subclass implements a shared `send(recipient)` method in its own unique way.  
- **Composition:** `UrgentNotification` sends the same message across **all** channels simultaneously.  
- **Dynamic Demonstration:** All notifications are executed polymorphically in a loop.

---

## 🧩 Concepts Demonstrated
- ✅ Inheritance  
- ✅ Abstract Base Classes (ABC)  
- ✅ Method Overriding  
- ✅ Polymorphism (Runtime Behavior)  
- ✅ Composition  
- ✅ Modular OOP Design  

---


---

## 🚀 How to Run
1. Clone or download the project:
   ```bash
   git clone <https://github.com/JD-Coder0129/Notification-System.git>

