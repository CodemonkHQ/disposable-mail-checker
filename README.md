# Disposable Mail Checker

A simple Python library to check if an email address uses a disposable domain.

## Installation

You can install the package using pip:

```
pip install disposable-mail-checker

```

## Import
```
from disposable_mail_checker import is_disposable_mail

```

# Check if an email address uses a disposable domain
```
is_disposable = is_disposable_mail("example@disposable.com")

if is_disposable:
    print("The email address uses a disposable domain.")
else:
    print("The email address does not use a disposable domain.")
```


You can also provide an optional list of additional disposable domains and an override flag:

```
other_disposable_domains = ["example-domain.com", "another-disposable.net"]
is_disposable = is_disposable_mail("user@example-domain.com", other_disposable_domains, override=True)

```

When the override flag is set to True, the function will exclusively use the provided other_disposable_domains list for checking disposable domains. This means that the default list of disposable domains included with the package will not be considered in the check. If override is False (or not provided), the other_disposable_domains list will be appended to the default list for checking.

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please create an issue or submit a pull request on the [GitHub repository](https://github.com/codemonk/tools/disposable-mail-checker).

If you come across a disposable domain that is not in the current list and would like to contribute, you can generate a pull request with the new domain to be considered for inclusion. Follow these steps:

1. Fork the repository on GitHub.
2. Open the `disposable_domains.json` file in the `disposable-mail-checker` folder.
3. Add the new disposable domain to the JSON array. Make sure to follow the JSON format.
4. Create a pull request to the `main` branch of the original repository.
5. Your contribution will be reviewed and, if approved, merged into the main repository.

Thank you for helping to improve the library and its list of disposable domains!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
The list of disposable domains used by this library is based on disposable-email-domains by 
Ilya Volodarsky.

## Note
Make sure to replace `"example@disposable.com"` with a real example email address for your usage instructions.