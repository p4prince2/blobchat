# blobchat

![PyPI version](https://img.shields.io/pypi/v/blobchat.svg)

A lightweight Python library for transforming and analyzing chat data.

* [GitHub](https://github.com/p4prince2/blobchat/)

* [PyPI](https://pypi.org/project/blobchat/)

* Documentation (coming soon)

* Created by [Prince Kushwaha](https://github.com/p4prince2)

* GitHub: [@p4prince2](https://github.com/p4prince2)

* MIT License

---

## 🚀 Features

* Clean and normalize chat text
* Remove emojis and special characters
* Word count and basic analysis
* Simple and chainable API
* More features coming soon...

---

## 📖 Documentation

Documentation will be available soon.

<!-- Uncomment when ready
* **Live site:** https://p4prince2.github.io/blobchat/
* **Preview locally:** `just docs-serve`
* **Build:** `just docs-build`
-->

---

## 🧪 Usage

```python
from blobchat import Chat

chat = Chat("Hello BRO!!! 😄🔥")
chat.clean().remove_symbols()

print(chat.text)
print(chat.word_count())
```

---

## 🛠️ Development

To set up for local development:

```bash
git clone https://github.com/p4prince2/blobchat.git
cd blobchat
pip install -e .
```

Run tests:

```bash
pytest
```

Run quality checks:

```bash
just qa
```

---

## 👨‍💻 Author

blobchat was created in 2026 by **Prince Kushwaha**.
