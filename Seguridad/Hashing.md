

# 🔐 Hashing Reference (Linux & OpenSSL)

This note shows how to generate **checksums** and **cryptographic hashes** using Linux tools and OpenSSL.  
Algorithms are grouped into “generations” by age and security.

---
## ==First Generation==

> [!warning] Obsolete  
> Use only for quick integrity checks, **not for security**.

### MD5
```bash
md5sum <file>
```
Example:

```bash
md5sum example.txt
```
### SHA-1
```bash
sha1sum <file>
```

---
## ==Second Generation==

> [!note] Safer than MD5/SHA-1, but SHA-2 family is the current standard.

### SHA-256
```bash
sha256sum <file>
```
### SHA-384
```bash
shasum -a 384 <file>
```

⚠️ Some systems don’t have `sha384sum`, but `shasum -a 384` works everywhere.

### SHA-512
```bash
sha512sum <file>
```
---
## ==Third Generation==

> [!tip] Modern & stronger  
> SHA-3 family is resistant to modern attack vectors.

### SHA3-256
```bash
echo -n "message" | openssl sha3-256
```
### SHA3-512
```bash
echo -n "message" | openssl sha3-512
```
---
## ✅ Notes

- **MD5 and SHA-1** → integrity only, not secure.
- **SHA-2 (SHA-256/384/512)** → current recommended standard.
- **SHA-3** → newer alternative, strong against collision/preimage attacks.
- Use `echo -n` to avoid an extra newline when hashing strings.
- Hash multiple files at once:

```bash
sha256sum file1 file2 file3
```
