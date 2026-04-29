# Test Cases

## TC01 - Valid Data
Input: valid device payload  
Expected: 200 OK, status accepted

---

## TC02 - Temperature Below Minimum
Input: temperature = -100  
Expected: 400 rejected

---

## TC03 - Temperature Above Maximum
Input: temperature = 200  
Expected: 400 rejected

---

## TC04 - Missing Device ID
Expected: 400 rejected

---

## TC05 - Missing Temperature
Expected: 400 rejected

---

## TC06 - Invalid JSON
Expected: 400 error

---

## TC07 - Boundary Low (-50)
Expected: 200 accepted

---

## TC08 - Boundary High (150)
Expected: 200 accepted

---

## TC09 - High Frequency Requests
Expected: system remains stable

---

## TC10 - Null Payload
Expected: 400 rejected