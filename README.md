# Butler Robot Task Management System

## Project Overview

This project implements a Butler Robot Task Management System using Python and ROS2 concepts. The robot delivers food orders from the kitchen to restaurant tables while handling confirmations, cancellations, timeouts, and multiple order deliveries.

---

## System Architecture

Components:

* Navigation Node
* Task Manager
* Multi Order Manager
* Dashboard Node
* Route Optimizer

---

## Scenario 1

Home → Kitchen → Table → Home

Successful delivery with confirmations.

---

## Scenario 2

Home → Kitchen → No Confirmation → Home

Kitchen timeout handling.

---

## Scenario 3

### Scenario 3A

Home → Kitchen → No Confirmation → Home

### Scenario 3B

Home → Kitchen → Confirmation → Table → No Confirmation → Kitchen → Home

Table timeout handling.

---

## Scenario 4

Task cancellation support.

### Case A

Cancel while moving to kitchen.

### Case B

Cancel while moving to table.

---

## Scenario 5

Multiple order delivery.

Home → Kitchen → Table1 → Table2 → Table3 → Kitchen → Home

---

## Scenario 6

Multiple order delivery with timeout handling.

Timed-out tables are skipped and remaining deliveries continue.

---

## Scenario 7

Multiple order delivery with cancellation handling.

Cancelled tables are skipped while remaining deliveries continue.

---

## Innovation 1 – Dashboard

A live dashboard displays:

* Current location
* Completed deliveries
* Timeout deliveries
* Cancelled deliveries

---

## Innovation 2 – Smart Route Optimization

Delivery routes are optimized before execution using route sorting logic.

---

## Technologies Used

* Python 3
* ROS2 Humble
* State Machine Design
* Queue-Based Order Management

---

## How To Run

### Single Order Scenarios

```bash
python3 task_manager.py
```

### Cancellation Scenario

```bash
python3 scenario4.py
```

### Multiple Order Scenarios

```bash
python3 multi_order.py
```

### Route Optimization

```bash
python3 order_manager.py
```

---
