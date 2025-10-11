# 🤖 AI Task Scheduler – OOP-Based Modular System

## 🔹 Overview
The **AI Task Scheduler** is a Python-based modular system that demonstrates advanced **Object-Oriented Programming (OOP)** concepts —  
including **Abstraction**, **Encapsulation**, **Inheritance**, and **Composition** — all within the framework of an intelligent task manager.  

This project simulates how an AI assistant manages and executes multiple background tasks such as reminders, backups, and computations.  
Each task is independent, reusable, and polymorphic — a clean blueprint for scalable AI system design. ⚙️

---

## ⚙️ Features
- **Abstract Base Class (`Task`)** → Defines the structure for all task types using `abc` module.  
- **Encapsulation** → Private attributes with controlled access for data protection.  
- **Inheritance** → Task subclasses extend and override the base class behavior.  
- **Composition** →  
  - `TaskManager` manages all task objects.  
  - `AI_System` owns a `TaskManager` instance.  
- **Polymorphism** → Each task implements `execute()` differently but shares a common interface.  
- **Realistic Simulation** → Backup process uses `time.sleep()` to mimic real-time execution.

---

## 🧠 Concepts Practiced
| Concept | Description |
|----------|--------------|
| **Abstraction** | Defines a common blueprint using `ABC` for all tasks. |
| **Encapsulation** | Uses private/protected attributes for secure state management. |
| **Inheritance** | Allows shared behavior with specialized execution. |
| **Composition** | AI_System owns TaskManager; TaskManager aggregates multiple tasks. |
| **Polymorphism** | Each subclass provides its unique version of `execute()`. |

---


---

## 🚀 How to Run
1. Clone or download the project:
   ```bash
   git clone <your-repo-link>

