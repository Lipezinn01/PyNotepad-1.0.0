# 📝 NOTEPAD - Professional Text Editor

## 🎯 FEATURES

✅ Save with ANY extension (.txt, .html, .py, .js, .css, etc.)
✅ Open files from anywhere on your PC
✅ **AUTOMATIC LINE BREAK** at 1024 characters (NEW!)
✅ INFINITE vertical scroll
✅ Horizontal and vertical scroll
✅ Unsaved changes warning
✅ Clean and professional interface
✅ Keyboard shortcuts
✅ CTRL+Z (undo) and CTRL+Y (redo) support

---

## 🆕 NEW v1.1 - AUTOMATIC LINE BREAK

**BEFORE (v1.0):**

- Upon reaching 1024 characters → ❌ FROZEN
- Had to manually press ENTER
- Interrupted typing

**NOW (v1.1):**
- Upon reaching 1024 characters → ✅ **AUTOMATIC BREAK**
- Creates a new line automatically
- Continue typing without stopping!

**Example:**
```
You type: "This is a very long text that will exceed 1024..."
[Reached 1024]
→ AUTOMATIC: Creates a new line
→ You continue: "...characters without problems!"

```

**Result:** Natural flow, without interruptions! 🎉

---

## 🚀 HOW TO USE

### Option 1: Run directly from Python

```
python notepad.py
```

### Option 2: Create an .EXE file

```
compile_notepad.bat
```

The .exe will be located in: `dist\Notepad.exe`

---

## 📋 FEATURES

### 1. SAVE AS...

- Saves with any extension
- Examples: .txt, .html, .py, .js, .css, .json, .md
- Choose the name and extension

### 2. SAVE .TXT
- Quickly saves as .txt
- No need to type the extension

### 3. CHOOSE TEXT DOCUMENT
- Opens files of any size Place
- Supports multiple file extensions
- Detects unsaved changes before opening

### 4. FORMAT
- Clears all text
- Asks for confirmation before deleting
- Message: "Are you sure you want to delete this text?"

### 5. HELP
- Shows complete guide
- "Got it" button to close

---

## ⌨️ KEYBOARD SHORTCUTS

| Shortcut | Function |

|--------|--------|

| CTRL + S | Save .txt |

| CTRL + SHIFT + S | Save As... |

| CTRL + O | Open file |

| CTRL + N | Format (clear) |

| CTRL + Z | Undo |

| CTRL + Y | Redo |

---

## 📐 LIMITATIONS

- **Horizontal:** 1024 characters per line
- **Vertical:** INFINITE (no limit!)

If you try to type more than 1024 characters on a line, the editor will lock.

To continue writing, press ENTER to go to the next line.

--

## 💡 USAGE EXAMPLES

### Creating an HTML file:

1. Write your HTML code
2. Click "Save As..."
3. Type: `index.html`
4. Save
5. Open in your browser!

### Creating a Python script:

1. Write your Python code
2. Click "Save As..."
3. Type: `script.py`
4. Save
5. Run: `python script.py`

### Creating a CSS file:

1. Write your CSS rules
2. Click "Save As..."
3. Type: `styles.css`
4. Save

---

## 📂 SUPPORTED EXTENSIONS

✓ .txt - Plain text
✓ .html - Web pages
✓ .py - Python
✓ .js - JavaScript
✓ .css - CSS styles
✓ .json - JSON data
✓ .xml - XML
✓ .md - Markdown
✓ .cpp - C++
✓ .java - Java
✓ .cs - C#
✓ .bat - Batch Scripts
✓ AND ANY OTHER!

---

## 🔧 COMPILATION

### Step-by-step:

1. Place the files in the same folder
2. Run `compile_notepad.bat`
3. Wait for compilation
4. The .exe will be in `dist\Notepad.exe`

### Generated files:
```
📁 YourFolder/
├── notepad.py
├── compile_notepad.bat
│
├── 📁 build/
├── 📁 dist/
│ └── Notepad.exe ⭐
│
└── Notepad.spec
```

---

## ⚠️ IMPORTANT WARNINGS

### Changes not Saved:

- The program detects if you have unsaved changes.
- Before opening another file, it asks if you want to save.
- Options: Yes / No / Cancel

### Format (clear text):

- Always asks for confirmation.
- Message: "Are you sure you want to delete this text?"

- Buttons: Yes / No

---

## 🎨 INTERFACE

### Top menu (gray bar):
- Save As...
- Save .txt
- Choose Text Document
- Format
- Help

### Text area:
- White background
- Monospace font (Consolas)
- Horizontal and vertical scrolling
- Size: 900x600 pixels

---

## 💻 REQUIREMENTS

- Python 3.6+ (tkinter already included)
- PyInstaller 5.13.2 (for compiling)
- Windows 7+ (for the .exe)

---

## 🔍 TECHNICAL DETAILS

### Font:

- Consolas, size 11
- Monospace (ideal for code)

### Encoding:

- UTF-8 (supports (Accents, emojis, etc.)

### Scroll:

- Vertical: Unlimited
- Horizontal: Up to 1024 characters

### Undo/Redo:

- Unlimited (CTRL+Z / CTRL+Y)

---

## 📝 TIPS

1. **Save frequently!**

- Use CTRL+S whenever you make changes

2. **Use "Save As" for different extensions**

- Allows you to choose any extension

3. **Take advantage of keyboard shortcuts**

- They are faster than clicking buttons

4. **The 1024 character limit is per LINE**

- Downwards you can write infinitely!

---

## 🐛 COMMON PROBLEMS

### "Python is not recognized"
**Solution:** Install Python and check "Add to PATH"

### The .exe file won't open
**Solution:** Run it from the command prompt to see errors

### I lost my text
**Solution:** Always save with CTRL+S!

---

## ✨ ABOUT

Text editor created as a project
