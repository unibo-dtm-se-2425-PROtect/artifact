## [1.7.10](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.9...1.7.10) (2026-01-12)


### Bug Fixes

* removing second encryption call in addEntry ([7e25ea8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7e25ea8fb54b6a65c81ee7fe44ab103a26da8f1f))


### Tests

* add helper function for hashing verification ([0f6fd1f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0f6fd1fe161d66bc89a9359a9fbbca5181ba5897))
* enhance AES256 utility tests with CLI cases ([fd71cde](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fd71cdecd9e40c45c0cc662c7aba031d49cc6663))
* fix mock AES encryption call in test_add_entry ([028d19e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/028d19ee90b44042e6f05d5016a356da8c07620f))
* fix test for wrong master password assertion ([805f2a0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/805f2a024c1cd81507d4e2bc67b1971fb66f7c42))
* fix tests to use updated AES utility functions ([bef7a94](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bef7a94adb4ea22acb34ca758f9e1eb346f38751))
* mock 'rich' module in test_AES256util.py ([7cfe0e3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7cfe0e3c4e5ee62f9df464706c3b0291e5f67c91))
* mock database row in verify master password test ([5979c0a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5979c0aaf558527858d8e044066bf46ed5f93f47))
* modify test for addEntry to handle empty password ([9458260](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/945826045be41d93725502a9c578575c034a24f0))
* patching modifications in test_add_entry_empty_password ([5a2fa25](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5a2fa257188d849c02c8b558b672e7afe9f22b63))
* refactor AES256 tests for raw bytes handling ([9efa972](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9efa9729677019c5859264db8b561e24f4c50bec))
* refactor rich module mocking in AES256util tests ([b78ffd7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b78ffd79cbf4898ef4141318bc9ca3ef13f7e2a1))
* refactor tests to use add.computeMasterKey ([0d50443](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0d50443d8f99f87b241cba600c08b3b8d347a6cb))
* rename and refactor master key computation test ([3108a62](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3108a62115fb39ef0705fc2901bde7ec12a5e3b8))
* update function argument in test_add_entry_empty_password ([a44c365](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a44c365c4a8ccbe5f4f6bba7c71082f49811bb4e))
* update test cases to use aesutil instead of aes ([15475f0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/15475f07612097652563191e83d8a8318695a54f))
* update test to use mock_row for database config ([fdcca1f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fdcca1f77005576e04a0e6ab316756b5af2ab43c))
* update test_add_entry_encrypt_returns_none to catch ValueError in the specific case ([b3d823b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b3d823bc51a337a3a12b575882f0509bcb95279c))
* update variable name in test for clarity ([51dea72](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/51dea72fb7d1537f35ddce9edc447f04a48b83ab))


### General maintenance

* adding a "guard clause" to addEntry to explicitly check if encryption was successful before proceeding to the database ([d8638eb](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d8638ebb78dbada03b79b1a40e82dd6285345b4b))

## [1.7.9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.8...1.7.9) (2026-01-12)


### Bug Fixes

* refactor main execution logic into a function ([f0510e8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f0510e893fdd63a1fedc20f5be91ed5e5d0561cd))


### Refactoring

* reshape main function and enhance decrypt output handling ([cc05828](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cc05828fbce91e014ff6e92c08cf240bb1683fb6))

## [1.7.8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.7...1.7.8) (2026-01-12)


### Bug Fixes

* refactor password retrieval from configuration ([e976c8c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e976c8c01eb651f3ba1258ddc723710ceb8b6ca4))

## [1.7.7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.6...1.7.7) (2026-01-12)


### Bug Fixes

* check source type before encoding in AES256util ([def0f7a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/def0f7a27dece5da821995083f6430266c746aea))


### Tests

* add password parameter to AddEntry call ([cb78de8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cb78de8c6f6d09d53c87068d9aaf04c26f9a846f))
* enhance test for computeMasterKey function ([2e19be5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2e19be57979a5e7df9724a17d3e327f2628195f7))
* enhance tests with parameterization for computeMasterKey ([22c66ff](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/22c66ffd52fd6468362141ce498b862eec32ccfa))
* fix AES mock usage in test_add.py ([b22aa16](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b22aa16c31482a2119b030df9e598f9c56e22319))
* fix assertion for 'site' in query check ([8f61760](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8f61760d1bc8f9c81c4c9570f422b07d36a8f4ce))
* fix import statement for AES256util module ([6fb3b50](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6fb3b50e628e5d3e4494dcc57e7eca7cfd34462b))
* fix import statement for AES256util module ([72d7b74](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/72d7b74811d4814759e71421670599b814e5e30e))
* fix module name in test for CLI reload ([cf8f320](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cf8f3208da526cbd80c735ab76f56c5dd49fd0a2))
* fix type mismatch in test_result_with_missing_columns_raises ([8b59103](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8b59103b1e0fee037ec1fe675fccd07c296da758))
* import pm from project.pm in test_pm.py ([e0c5757](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e0c57570f012e2e0ff46c099a7bf14d4fa19ff96))
* modify site existence assertion in test_check_entry_exists ([cf8c4c0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cf8c4c07f17e26324f9bebeacc1994502be9b1a6))
* refactor argument parsing into get_args function ([0ea001e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0ea001ee9f0e430770118d56960018f212077c62))
* refactor import statement for project.pm ([30408f8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/30408f89e4589fc6e1eab131e8739e0e79491500))
* refactor reload_cli_with_patches for dynamic module import ([9d9f617](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9d9f6174f268bb770e1d8a482d044228a99eba8c))
* refactor test data to use dictionaries for clarity ([cbaf33b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cbaf33b6ea39c9386d3a5cf28136cdf623f0fd03))
* refactor test_single_result_decrypts_and_copies ([b197660](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b19766089ac2edf132e75ab4b73b6ad8e00d799c))
* remove unused import of AES256util ([929ccd2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/929ccd2f2e80287a49a42dd0c338573be0bdb54d))
* rename import from pm to project.pm in tests ([cdfc83b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cdfc83b3c6eb763a03ed2afe162e121ef1efd810))
* update module import to AES256util ([0727fc2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0727fc2eb89bdb52aad0790bb472f4793dbd7378))
* update module reference from 'cli' to 'project.cli' ([d8d9fb5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d8d9fb5f00bcfd73d7d55fed913a7660f35d385f))
* update module reloads to use AES256util ([54a2635](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/54a26353065af1307031330cb39bade882ec7edb))
* update test to use dictionary format for results ([ddddf4f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ddddf4fcc6649ccf9601a92925080cf4330465d9))


### General maintenance

* import the getpass module  ([57b6ec1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/57b6ec11ba984efbe9e198feeafdffab679e0aec))
* raise ValueError if Password is empty in addEntry ([44344f7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/44344f7a0db273c4fb7e6633ecdb4ebf7fc9751d))
* rename variable enc_pass to enc_bytes  ([fc8e862](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fc8e862f82ba96601ce1b6d9e9e6f73e23764849))


### Refactoring

* add argument parsing to main function ([502f389](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/502f389ce008b62805497f891b85c9aa6fffa163))
* add main guard to pm.py ([ac26c5c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ac26c5c40e2c770ce9b73f43ecc6092452a6f9eb))
* fix formatting of argument parser help text ([aa53f98](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/aa53f98bee744967ddce3cc3e8a929d7955ca029))
* refactor argument parser for clarity and help text ([684d916](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/684d916ebb1c9ae292060ce504c2f5f5b3ff076c))
* revising password table row addition for clarity ([fd7e047](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fd7e047ad2e4acdba503b20db678153b5ef2390e))

## [1.7.6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.5...1.7.6) (2025-12-08)


### Bug Fixes

* changing test_fast_computeMasterKey_edge_cases name into test_test_computeMasterKey_edge_cases for consistency ([398cb4e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/398cb4e0cc9f4b2a1e20c7eb47460c26cebe9958))
* modifying referenced function in test_compute_master_key_invalid_types ([72ac1e3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/72ac1e361bfbe515f5097587ba2f55e0990eeb35))
* modifying referenced function in test_computeMasterKey_return_type_and_lengt ([e2ecbd4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e2ecbd4bf874290ab6ad06f1cf2e310747653b22))
* modifying referenced function in test_computeMasterKey_type_errors ([12eb102](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/12eb10296c70f28e1467c16aef62adeded9dd881))
* modifying referenced function in test_deterministicOutput_and_uniqueness ([349c0db](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/349c0db7164922bd178c7a082670c04565dffd28))
* modifying referenced function in test_fast_computeMasterKey_edge_casestype_and_lengt ([e256d42](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e256d426648edd8a026e2e914982d9dc0c4a9efc))


### Tests

* add _inject_dbconfig_module function ([e2201a8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e2201a8831d70ac8137feab501fbdc5aa468a569))
* add imports needed for test_AES256util.py ([a6e2022](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a6e2022525f4802b6604b11610429c1ddc4dda8f))
* add test for checking verify_master_password behavior when a stored hash exists but the provided master password is incorrect. ([8a1d16b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8a1d16bd9070bd9270bbd2131b064e96bcbbe197))
* add test for checking verify_master_password behavior when no configuration is found ([92bfc42](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/92bfc425457919f1a17c24dabb900818a3405af4))
* add test for checking verify_master_password behavior when the provided master password matches the stored hash ([4c8c21d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4c8c21db6d303bcae9f2653495735b6279292aa8))
* Add test for computeMasterKey function ([9776cbd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9776cbd9e3e2cde92e713f9683c5f70323fc41aa))
* add test for confirming that tampering with ciphertext raises padding/integrity error ([2dc43d9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2dc43d9ef5100e0dc6f222c76a56530e3bacdde6))
* add test for documenting and asserting current behavior when encrypt is called with encode=False and decrypt is misused with decode=False ([a590778](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a59077889b3cf948f919607fa45838df850ca394))
* add test for encryption and decryption roundtrip verification with ascii key ([61aa0e8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/61aa0e8e4f6aaeaca2306bc119736646a2a12339))
* add test for encryption/decryption roundtrip with hexadecimal key ([331cbb9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/331cbb924e07f6655384d9a708d628ec793cc103))
* add test to ensure padding is correctly handled for messages that are exact multiples of block size ([23980da](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/23980dacee306b08f585d8680d2610e6720fd9ff))
* changing the cryptography module from Crypto to hashlib ([62f32e1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/62f32e19e84810c3e87672c701e87950c569b6e1))
* create a dbconfig submodule  ([ee278c1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ee278c1647a0bd24c79d95798c8f432ddc6e95d3))
* create the cleanup function ([3ba9e4f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3ba9e4f0e0ee93fdd4e8522f22ea1fa7b969c67c))
* implement _reload_aesutil ([3308b34](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3308b34701d11e08d443812fc80b53db35c22c16))
* implement test ensuring clear_fields behaviour is correct ([877f84b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/877f84bcf74853e4dfa5605da800cb491b9cc68c))
* implement test for LoginApp functioning ([cb0767c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cb0767cbfc2e816258abe25cfe96e547147684ab))
* implement test for verifying success branch of verify_login ([a2d254e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a2d254e818973a71ce01aaaf804a67fc0dba6384))
* implement test for verifying the failure branch of verify_login ([d1de819](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d1de8199e1787e07ea952dff94e826a2afe9f457))
* implementing FakeCursor class in test_AES256util.py ([fb84748](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fb84748095ca935ce0983627f2906c0a87e1aff9))
* implementing FakeDB class in test_AES256util.py ([8674e22](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8674e2252c522ca7f9899f1e1f788e7ef3e96d5a))


### General maintenance

* create test_AES256util.py ([b834da9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b834da901447e066debb01baa236ba45880aa5cf))


### Style improvements

* adding a docstring to summarize what _inject_dbconfig_module does ([0758873](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0758873c12d02bf0dbcf876a5a774a06b0d44421))

## [1.7.5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.4...1.7.5) (2025-12-05)


### Bug Fixes

* docstring indentation correction  ([1f614ea](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1f614eaba2716dfd55bbcae4d5c02c3970bee5a6))


### Tests

* added "bind" method to FakeRoot  ([2a1f4bf](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2a1f4bf0ae56df1b7d9201788c543f5745af3de1))
* added "geometry" method to FakeRoot  ([f7d77ab](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f7d77ab1555fca6b5d0deb47471f334ceae93e71))
* added "title" method to FakeRoot  ([1e57625](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1e576255c26ce073ec9e0b8ff51eb4c3a042e5c9))
* added FakeRoot class ([08e54c7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/08e54c709fe9736dec936d8e65deb3706d1f026d))
* added FakeStyle class ([37e751f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/37e751f046d627a0f158898377835ac1c651e17b))
* adding a patching helper to centralize the previous mock patch objects ([bb43b49](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bb43b496456c0238a793ea66069b625d2e7b7e5d))
* implement focus method in test widget class ([ab7351f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ab7351f8c3d92a505d48a9c8cf4d018387b11cc7))
* introduce FakeButton for ttk.Button simulation ([5bae482](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5bae4823b3b94d17f0537e52c3bedbaaf43b1fde))
* update FakeButton class with "Invoke" functionality ([946443d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/946443dcdf854c8176178696dc245035ee565bbd))


### Style improvements

* adding a docstring to summarize what FakeRoot is ([a408405](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a408405d9229e355a4d49ca9f72217c0865a4096))

## [1.7.4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.3...1.7.4) (2025-12-04)


### Bug Fixes

* indentation error with docstrings ([959d002](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/959d002f92706ea1bd7b5ddffa1a0e6e607feca2))


### Tests

* add FakeFrame class  ([66f6790](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/66f6790676382c4a4e59bf53a8c228d6d4edc83e))
* add FakeLabel class ([70ab9c9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/70ab9c972a0e271421ba160e999cc8166e5c1345))
* add get method to FakeEntry class ([8b6ab3f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8b6ab3fa2e489f6e9e99efef070bfde7eeda2e7b))
* add imports for pytest and mocking ([4e4297f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4e4297fb0466e4ce38f884d2527fd38c79ab03a4))
* add necessary imports for tkinter tests ([c0400d1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c0400d1d5ae194d358caff5037efed0298d89204))
* add pack method to FakeWidget class ([f2556a4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f2556a46d2bb0a78c1ef6ccb10086ad8fd443eb9))
* add reload_cli_with_patches utility function ([5df1f8f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5df1f8f1cdcd60e1b63b3b85749412453731631c))
* add set_value method to FakeEntry class ([b8bfd82](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b8bfd827e949012fdf88b8439baba639b0d14406))
* add test for remove command with ID ([0bd3a11](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0bd3a118f1e746ec68b310e54cd49341b6f98831))
* add test for successful import of entries ([bda1efc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bda1efcbfee3a0496ecab2388bb61bcbf4896250))
* comment addition for explainability ([ce4ce11](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ce4ce11fb42ec48a2cad4070ec19009cc6f71a98))
* create FakeEntry class  ([83282cc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/83282cc3101276438e18a341317faa145ae80ed0))
* implement delete method in mock Entry class ([6fb3da4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6fb3da4d484a2a776aba87bdd4bcf8287a6f3492))
* implement FakeDB and FakeCursor for tests ([15b7edc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/15b7edc4933f1538accaf3bb9ad225955c503657))
* implement FakeWidget class for unit tests ([3ed6902](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3ed69022ed7164dbe224c7d1c6b676a4211532a2))
* implement test for add command with missing fields ([2b56812](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2b568128db7d95228825309fdde14fc0f6125aa8))
* implement test for addEntry function call ([484f415](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/484f41581928e8cecb03f6eb5e47dd6aa23d26dc))
* implement test for empty filepath error handling ([d40d743](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d40d743efe7937a8e30833db5f835dba08501b4b))
* implement test for export with file argument ([23e13a5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/23e13a5bbde55ac9a4f178188e2e7d327e55b146))
* implement test for extract with --all option ([7e2892a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7e2892ada560f1dbf7518e0a8f594d4a9e37826a))
* implement test for extract with search fields ([7ab79c5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7ab79c57942138cb5f30d691625e6a559648a86e))
* implement test for falsy master password scenario ([8991ddd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8991dddd18081847499982fdf6bc6d76ef97945e))
* implement test for file not found scenario ([d642b44](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d642b44879f7b892b48840667fadcc5653f79e24))
* implement test for generic exception handling ([9f789ae](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9f789ae98e9e1c0101b1f0b61f0e85eba117a6ca))
* implement test for import with file input ([7938af4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7938af43bf9d1d31f41e3a7dc25c83bd412c5b68))
* implement test for input master password success ([70f1a0c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/70f1a0cecabe575a8d178946f1063d325c36283c))
* implement test for missing file in export command ([54af73e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/54af73eda39e7660a151fc348036d77037bd5b77))
* implement test for missing file in import command ([4537928](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/45379284eef2dc18ad075e65ca5f9bef5dd52736))
* implement test for missing ID in modify command ([c6b1ab6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c6b1ab6dd648de3a945a5b78424dbeb2c81faa24))
* implement test for modify command with ID ([538cdb8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/538cdb829935d487698dfda540d90a5666a7d447))
* implement test for no search fields in extract ([34e2f94](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/34e2f947c9fccd3ad9a3660ab2a87c5b675b292c))
* implement test for remove command without ID ([97477ec](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/97477ec3ec68eb9824fccf86e6936dbe9602b9e1))
* implement test for skipping incomplete CSV rows ([873b43e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/873b43e14e9328a56c9dd4a4d0552f64e4113879))
* implement test for wrong master password hash ([8e99d25](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8e99d25f196952676256206298524ea4b40bc4d9))
* implement test_extract_no_master function ([0bc6efa](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0bc6efa936d34b8111527c1e4d80ad626a67c1d5))
* implement tests for configuration commands ([ff9312e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ff9312e1099591ca85255553bc79efdcfeca4010))
* implement tests for password policy checks ([7cfc149](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7cfc149d644c3d1ce17ff81adde5ca59c504592b))


### General maintenance

* create test_pm.py ([b0297b2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b0297b2c0f352157585c6bfb0c947d8362c270c6))
* create test_tkinter_bootstrap_sample.py ([6c03fdb](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6c03fdb331b9fde48b3c8b895918edd65d702ce9))


### Style improvements

* define docstring for FakeEntry class ([3bc5b50](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3bc5b5063783f28419227fc9fbe545e420aa8b35))


### Refactoring

* change in "secrets" table's columns' semantics and hashing method to make the SignUp and LogIn work (only the SignUp worked, problem with stored master password hash) ([b1b79d7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b1b79d7e61539d1e9dbd22db05d691684af5a6dc))

## [1.7.3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.2...1.7.3) (2025-12-02)


### Bug Fixes

* typo (missing dot) ([0fb5d8e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0fb5d8e6d9b26c41c193f2169c1cc1cf9c6d015f))
* verification method of the hashed mp at Login ([48b17d5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/48b17d539433c045ed02f62046b7b86ee6cdbfa0))


### Tests

* add DummyCursor class for testing SQL execution ([192484b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/192484b1e3c263f137ab8e1a97db42604745da85))
* add imports for CSV and mocking in test_importf ([34f3ee9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/34f3ee9b61cfbf2a809143fee9cf621d200b7958))
* add make_csv_file helper function ([8182e80](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8182e80370903171b018530fc599a1a3df7ee589))
* implement DummyDB that mocks a database for testing purposes ([5fbee02](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5fbee02519611c8ebe7ead04e2bf787d8836dbf8))


### General maintenance

* adjusting imports to make functions work ([a0ea374](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a0ea37426e3098b3adc307e637ff6ed854ec023e))


### Refactoring

* naming convention to let the --test mode for GUI work ([60387e4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/60387e4604fc971d3511d07bfae41a667d791f73))
* only one dash for maintainability ([efa417e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/efa417e3cec68f5cb46cab706670ba4d919d0b42))

## [1.7.2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.1...1.7.2) (2025-11-22)


### Bug Fixes

* found VARBINARY error for MariaDB rules that made (re)configuration unaccessible (varbinary wants number of chars) ([6ffc469](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6ffc4695980452cb244575f25a4bfce9ef09b820))


### Tests

* add imports for CSV and mocking in test_export.py ([b0a015d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b0a015db871d71019d0971b66bfbcc3990bb581a))
* add test for exception handling in export_entries ([9744b9f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9744b9f1bc10c33e4bc7b981c3a53b17e0c041d6))
* add test for export_entries_cli with password check ([291fe37](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/291fe37003db8c5c0322223233d53a14ede455d5))
* add test for successful export of entries to CSV ([b0ede27](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b0ede275af86d2109df8c94a1b2e955732eb28d9))
* add test for the success case ([1d7a01d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1d7a01d4c2d9c8a5b8a4c7508acc8c8c65511014))
* implement test for DB connection failure in export ([ad3f3b7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ad3f3b7ebe5cf69d16efa514e093ce994cef0510))
* implement test for empty filepath in CLI export ([9b36396](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9b363969683797b266f6ddd8dea7d040fd526d30))


### General maintenance

* adding right path for file imports ([1d00e5f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1d00e5fcfef65721ca50bf41581e93cb65567f2c))
* change the name of test_import.py into test_importf.py  ([ebff2fc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ebff2fcef9cf1181de0da4aad79e19e2e1347608))
* clarify comments in test_export.py for the test_export_entries_success_writes_ function ([5d2497c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5d2497ce0deb83f8ec958eb45747f57cf3b50e56))
* correct path for import modules ([46182a2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/46182a24eb7dee1921e8013cc4c66f73ec021c74))
* create test_import.py ([773e179](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/773e179ba673e2d4ad2a1af44be6eadb0dd48b42))
* naming convention for variables ([80887c9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/80887c9b64120d0659d9d972751407b8485bbb24))
* rename importf.py to import.py ([a3fd416](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a3fd416a7ae6c829531cfb113c0607ae1ebb8aec))
* right import path for modules ([4bda49e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4bda49ef1aa5d8e12bc1ad4351c853149a5c642c))
* set the file name back to importf.py because of library-importing issues ([1ce9902](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1ce990216788236edee15f4f5ea8b216f6aceb90))


### Refactoring

* allowing both options of config and reconfig DB based on selected system argument ([0b7c76f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0b7c76feedacc0dbd97954d83913f3adcc5ff4e8))
* enhanced implementation of ds handled by the Login Controller and better defining linkages to Login Model ([de9c4a1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/de9c4a1307b276a40622f0419064cfa656570dd5))
* remove unused redundant _secrets_has_username_col function (intended to handle DB inconsistency, but is unnecessary given it is already enforced in the code structure) ([3fb2a66](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3fb2a66a2088b503215481b55cd121895951c47c))

## [1.7.1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.7.0...1.7.1) (2025-11-18)


### Bug Fixes

* try to change distutils.cmd with Command because it can give problems in some python versions (cause of the wrong release on PyPi?) ([bf371b3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bf371b357fd3178a8ac6e09582a2ed1b9ef40469))


### General maintenance

* create test_export.py ([a0545e8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a0545e825fb3bc920a69fd0c844477b2b42af288))
* remove unused imports ([38b5dbe](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/38b5dbecfacd8c5ea838e3af20c3fca804273116))

## [1.7.0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.6.2...1.7.0) (2025-11-18)


### Features

* **crypto:** implement double check security mechanism in GUI controller for sensitive ops ([a40a4ed](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a40a4edf087c6da90b67ba1c4a4e8f389e22b66c))


### General maintenance

* add column for ID in the visualization (but keep it hidden from user because he does not need to know the ID to perform operations like for  the CLI) ([c6c04f2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c6c04f2c4e5aeb73ca711b7f406dbda142374b4b))
* decryption logic for password when exporting files ([20a6b82](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/20a6b824fd871cda05335cb7b9652245e7692bac))
* switching from TEXT to VARBINARY for the password in entries table to make CLI and GUI match ([32ea990](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/32ea9901499715a0fd6a7f1c9941b99b8a882911))
* type hint for the ID field (int) ([1451e7f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1451e7f838bc31ce2549af64dc283cd7d1ea42e5))


### Refactoring

* implement Login MODEL and change references and imports ([f423b32](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f423b3296981096c54c81638125135fde39135a3))
* implement Loginmodel.py to input in the controller ([7303d3e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7303d3ef9d20b9a0ef0837bd9544ff3f6736725e))

## [1.6.2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.6.1...1.6.2) (2025-11-17)


### Bug Fixes

* adust encryption/decryption logic ([1d82a93](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1d82a9356f28d1a74ba7605e7c96ff7bb5fdeb7c))

## [1.6.1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.6.0...1.6.1) (2025-11-17)


### Bug Fixes

* typo in file extension csv ([6227711](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6227711aab3c252016d23a538e8fdc08a3451601))


### General maintenance

* delete not accessed class timer from threading ([fa36377](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fa36377a0108abb645e47ce78d8464426f6f9d01))
* delete show_message function (an error) and point to the right show_password function for command on_show ([56e9864](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/56e98642dce2496d170b59c25f6ba2ee48efcee2))

## [1.6.0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.5.2...1.6.0) (2025-11-17)


### Features

* add function to check whether an entry field has not been inserted (among the required ones) ([1a15359](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1a153594c9a82ee7c20f54256b719284869553fc))
* **cli:** integrate delete, import, export, and modify commands via pm.py ([0aa458f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0aa458f4c05cd126e3054e27391f6f2ec8009a5d))
* **crypto:** add device secret usage in master password verification and update all dependent operations ([5270a4f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5270a4f09c69a02f57d645b9a21327ca72f344ff))
* implementation of the modification of an entry in the CLI logic ([86d1fe1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/86d1fe1380bf361e978487413def3e7766be4fc7))


### Bug Fixes

* adjust import syntax (to make import of AES256util work in tests) ([047665a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/047665a944974e32180c83d3792ac416aa0fe5ea))
* brackets ([79f6fb9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/79f6fb99a0934095ad6f95834c7ba34957673a5c))
* **crypto:** use cryptographically secure Random Number Generator for device secret ([38986fa](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/38986fa00a247a52283b5dfed7a4e08d6bb5c418))
* insert into secrets table the mandatory username column (to recognize which password identifies which user) ([ad58e6b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ad58e6b38d1566486452ea6bcd6cfb88bfd00cf7))
* propagating username parameter and passing username and ds into main and test mode for entry point for GUI ([c393e03](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c393e03212e0d504c4db28679d5a791071de54c2))
* renaming delete configuration and remove an entry by ID to avoid misunderstanding between the purposes for two deletion operations ([9bb4edb](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9bb4edba104ac11d7fd10637013f9e8e27f148c3))
* secure password retrieval and mask in results table ([94266ac](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/94266ac5b2c6a768f82b6cea8b260b245b2f145e))
* values to return to edit entry ([52fbd76](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/52fbd76163570d6339955a5baafd239764ccff48))


### Tests

* add imports for pytest and mocking in tests ([2f7498e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2f7498e3c6ec2655b42928ea5411ed6ed820c641))
* add test for addEntry when the entry already exists ([860b26b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/860b26b4e0874e98ddae18d92ab4419d999436ae))
* add test for checkEntry with mocked database ([d2a42f1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d2a42f154305aecb74cee9f6a97a91fe19e47624))
* Add test for fast_computeMasterKey function ([e82e92e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e82e92ec90a78c01725453cb45ac4aceda8289cb))
* add test for multiple results handling in retrieve ([06a1f6b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/06a1f6ba14a9171c7198cbc6dfaed158f14889b7))
* add test for query without search  ([1738238](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/173823891de2e19f73b99b4ea1afccc4b5ea4077))
* create fake_cursor fixture for DB tests ([87c8070](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/87c8070617cca68c5f0c907482d96b979833b463))
* create fake_db fixture for testing database interactions ([542f2fb](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/542f2fb32654d1a9a4f6382d136c3a717b7131fc))
* creating function for quick master key computation ([f70b26a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f70b26afac032cb2f74a195334811d289f26823e))
* enhance test for addEntry with None encryption ([c771803](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c771803ff36fab5288c58ddfb1b55e70e647bdcf))
* enhance tests for computeMasterKey with edge cases ([64dd952](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/64dd952d52a7815e80faea441b238ad50e95351a))
* implement SQL injection test for checkEntry ([12b10d2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/12b10d222b6f8039b66992178504949eca259a5e))
* implement test for addEntry commit failure ([54d7bc2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/54d7bc24902d5afdb6cef2dcdd6d27208af49361))
* implement test for addEntry with invalid key type ([b636d45](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b636d45561caa268372d6d0e888dc0a6b18234b7))
* implement test for computeMasterKey function ([93ddc2c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/93ddc2c3784e3d1181ce3cbcbcbf1426066b1b7c))
* implement test for empty password in addEntry ([125056c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/125056c856f8e6ecd86ab5a59e1091dafbd12f71))
* implement test for empty password scenario ([2293432](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/22934320d060c7d877f427f9012c7197527c32bc))
* implement test for encryption failure ([cfe95ab](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cfe95aba046eec63b93f6433001fde8f4c7dccbc))
* implement test for happy path of addEntry function ([ce977ed](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ce977ed1f27150f5c3a848f76d5a5648ed7f9b01))
* implement test for invalid input types in computeMasterKey ([5c4f6e8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5c4f6e8e393e8a3b73f432efc8a9b88b97bb2578))
* implement test for missing password column in retrieveEntries ([c6cbfb6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c6cbfb6099c84aed04b70d1b7e1a56185823eb94))
* implement test for multiple results display ([cdcfc87](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cdcfc87a6166e9e330e67d17eedc2e77b6c9c922))
* Implement test for no results in retrieveEntries ([d87b86c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d87b86c8d5e41afe130c782bf4991338f14040df))
* implement test for non-existing entry in checkEntry ([dbb05d2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/dbb05d26e90656038c9366a1abe0389fa370eaf1))
* implement test for retrieveEntries with search ([6b9d995](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6b9d995b0220900dbcb7171c1e5eeeb26db695b5))
* implement test for single result decryption and copy ([ecb466e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ecb466ed5211fde7ee29ddb3ad0d9abc8eea320b))
* implement type error tests for computeMasterKey ([2752408](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/27524083be023a59af0dd9a4a5055f5333c16f84))
* update test for no results in retrieveEntries ([87308e9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/87308e9b8b70888b05b571653860102cf16aa3e5))
* update test to use fast_computeMasterKey function ([ecf5b79](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ecf5b79209e5fac5a9dd18e869e45f626108a11e))


### Build and continuous integration

* updated version 1.5.2 for new PyPi release ([2e33a1e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2e33a1e7a31584c242445708bfe609cf41694a7d))


### General maintenance

* add ID and username into secrets table to connect a password to the right user ([f7e6e23](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f7e6e23f61c1ac5177fec293273e496b3f736d72))
* add make_fake_db function for test setup ([024a610](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/024a610dc4ff3e053c33efb68d6dc48e1249c2ae))
* add PYTHONPATH environment variable to test job ([fb783f3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fb783f394aacf42f753295cf5d44b408185e8a53))
* add test for successful entry deletion ([076e0f3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/076e0f3874121f3fb004d293ca2a9806fa2df837))
* adding missing column for ID ([44d639d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/44d639dab26fd23b88145256aadb69e0b8788aa1))
* adding user reference to verify master password ([6a76edd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6a76edd403b6f17212576f200b7dc8426c32ef53))
* adjust constraints to fill the result table when retrieving entries ([c0a9273](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c0a927320e870dafb962ad5f9b459203a1c4fc1c))
* adjust encryption logic with hex ([78c4606](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/78c4606ad1325ed51115295b7d9bc46b537ab870))
* adjusting add_entry logic concerning password field management ([836f54e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/836f54ee98c9e01e4cf66d26a94cecb652cd9a9a))
* adjusting DB access ([a71a050](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a71a050be627fffec54a806c5e258ac95ab318e6))
* change from hexdigest to digest to return bytes ([bd2c16e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bd2c16e96d3207a50dc85cd9dc5d66dd20dda586))
* change mk to hex because the function expects the hex format (and then it will change format into bytes) ([4636523](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4636523905dd4b69b686d7dd1e9f97987d2f6628))
* changing import syntax to let tests work ([0c8b766](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0c8b766134db9e1eb520ca0914d6df4f736dd79e))
* create test_delete.py ([a738238](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a73823868c53d3717372dceacd93ce2bb7449f5d))
* create test_retrieve.py ([d11d940](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d11d940689c300cfd7f0d1644d1f6b81b065912e))
* creating test_add.py file ([2d145f1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2d145f12c154c688bc6847d830eff001b41d3f7d))
* delete repeated imports ([c808f58](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c808f58441c5599b7891ac9ea7683aedd227421f))
* enhance test for delete_entry_cli with exception case ([6c88ca3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6c88ca3e29dede6b26465104ead5fff08893a01c))
* implement FakeCursor for database testing ([00f2f32](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/00f2f32f82e639ec24cf33b6006f8c9a6c4becca))
* implement FakeDB for testing database interactions ([4446401](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4446401f7490bfe6086be965a503ca8c8c282eaa))
* implement test for delete entry cancellation ([87121d3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/87121d3e1f2083353839770df7c63966369b8a4b))
* implement test for delete_entry with no rows affected ([3c11bc4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3c11bc4f2c8d854e479275d22169410e8fb9eb1e))
* implement test for exception propagation in delete_entry ([c0a0eb3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c0a0eb32b584793f0fb39a4f3fd046514faa771b))
* implement test for invalid ID in delete_entry_cli ([d2055dd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d2055dd2914ea1f964b3ca4592e9f2ef76d9de73))
* implement test for successful entry deletion ([6c96679](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6c96679d1d2ac1be056edda3ecc689e6438d0bdc))
* import necessary libraries for testing  ([306b811](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/306b811781d7ad2931d397035d38cd50ba6f37ac))
* modifying the previous commit into: test: importing the needed modules ([3860053](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/38600536a54d1d1098b47d2ff6c9fad0c6ffb238))
* pass the device secret (stored_ds) in verify_login ([403f5bd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/403f5bd726ef20759f6fbc95e1c3195e2ac0b1a4))
* passing ds into init and computation for masterkey ([e3fe8a4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e3fe8a4c1b09b720154d3583b48f776d9b5ac35b))
* remove import repetition ([d4da123](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d4da123f8a2ae4d23f9877e43055e3ddbfe2b53b))
* removing redundant setting of the password in the new entry ([240503f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/240503f7dd006aef43db6431e72c80bf12c62b39))
* retrieving the dictionary ([4e6c281](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4e6c2814cc38dfb0d5f34e7a6cf06510f320d903))
* specification to avoid "encode" error on a source that is already in bytes ([8b810c8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8b810c879d8a794440b8771955f706dd1fed50a4))


### Refactoring

* fix function definition syntax in test file ([40d9671](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/40d96711a30173d0a84319d0603bcfeb25e7be94))
* fix import path for AES256util module ([00eb43f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/00eb43fde8064cd5c0105fd94601a659d6c85592))
* fix import path for AES256util module in export.py ([a590094](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a5900945cf26c20ec62ad23f6a7e6cc3c7badb7e))
* fix import path for computeMasterKey ([e9d306e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e9d306ec37c6807b9f6ac3702044557ae6ba53a4))
* modify verify_master_password to return device secret (and simplify call in all affected modules) ([72ee18c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/72ee18cfd8fd0b25b306b0ee41c00a16e5d2be0a))
* new name "importf" to avoid conflicts with "import" in the python library ([5f06dc2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5f06dc22476bf84ea8aae7709e807f2dd9513890))
* propagate master password and device secret to function calls (with new implementation of verify_master_password) ([b6040bc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b6040bc6fd35adcb541ba582401373ffa771ddaa))
* rename import.py to importf.py to avoid python module name conflict ([774ccdb](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/774ccdba2a9acf2cc1152324913ce468bf7e1b95))
* unify naming conventions across authentication and DB ops ([fef3fa5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fef3fa5de299228ca0ad32626cdf8249df08332f))
* update import path for AES256util module ([3bcb7cc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3bcb7cc1478c7dfbc4de9e1e1db86be1e8085617))
* update import path for AES256util module in delete.py ([7841273](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7841273bad3563d067613cd290429f9affe603bc))
* update import path for dbconfig module ([82fb916](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/82fb9162c5daf55f303958eaf696f3b6dae7385f))
* update import path for dbconfig module in delete.py ([bd4b3cc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bd4b3cc40655164ce969360c6fcc8d8d36e400f3))
* update import paths for dbconfig and AES256util ([76a2864](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/76a286469f01f23d751709a8982e630265c5d3b4))

## [1.5.2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.5.1...1.5.2) (2025-10-18)


### Bug Fixes

* typos and wrong parameters to make the GUI work ([f8faf26](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f8faf2639e15e79b5f8af33e3dc2080f0da449d6))

## [1.5.1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.5.0...1.5.1) (2025-10-18)


### Bug Fixes

* typo ([1c282d7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1c282d788017e9d688249cd945b811343e251403))

## [1.5.0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.4.0...1.5.0) (2025-10-13)


### Features

* **cli:** add command-line interface for modifying entries ([6722315](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6722315c9c6374b88fa540090868b8c6eda2fe5d))


### General maintenance

* updated version ([6ade650](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6ade65039b88adfdd5eab1969d841f9054fb7091))

## [1.4.0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.3.0...1.4.0) (2025-10-13)


### Features

* **cli:** add import functionality via CLI ([e9ee9bc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e9ee9bca8a9c207e779347d71bdcc51a3a207ef9))


### General maintenance

* automatic version update ([892bf20](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/892bf2094e6122e998d462d86dd0a2b9ffc3212a))
* decrypting password ([9553534](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9553534e99d47a0bce7232e840db9d192f55fcee))

## [1.3.0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.2.0...1.3.0) (2025-10-13)


### Features

* **cli:** add export functionality from the CLI ([d8c26e8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d8c26e8148e4d707d3c3281f91417e728d316625))


### Refactoring

* defining the verify_master_password function inside AES256util so that it is tied to encryption/decryption and security logic and it can be accessed easily and quicker by all the files that need it (consequently revising delete.py since the check on the mp can be done from the outside now + deletion of control on ds) ([9ca2c88](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9ca2c884894c8a5dfeae00d856008e95e1e27b3c))

## [1.2.0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.1.1...1.2.0) (2025-10-13)


### Features

* **cli:** add "delete" command to delete a row via ID ([871b277](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/871b277b14b1efee96e0fd6ecaed8408a23cfa8c))

## [1.1.1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.1.0...1.1.1) (2025-10-12)


### Bug Fixes

* spaces in name ([0a4617b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0a4617b89d081a88865eeba4fd0446be5d8fd526))


### General maintenance

* deleting temporary configuration for not running tests ([272733f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/272733fcdd3258e9f12dbef6706dca4e5f5884fb))

## [1.1.0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.9...1.1.0) (2025-10-12)


### Features

* command to modify an entry (a single or multiple fields) + various errors handling ([5881068](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5881068f09aad0281b4c1005d362399deeea9033))


### General maintenance

* add primary key ID to ENTRIES tables ([568b936](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/568b936239c4b47ea8783c89fb087f6935888eae))
* **cli:** improve error handling in add.py ([2c844de](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2c844ded96b01860828bace1f40da7da6b3e3bac))
* create new file for command to edit entries + imports ([705ade4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/705ade44c0cb2dffa249a9f26532e406414d079b))


### Refactoring

* delete repetition of ComputeMasterKey (already imported from add.py) + delete useless import crypto libraries for its computation ([067eef2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/067eef2f06ea0c49124b5946f2c3e6290a941480))

## [1.0.9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.8...1.0.9) (2025-10-12)


### Bug Fixes

* restore generation of the device secret ([920749e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/920749ee37889028247cc430c5a4d78762012cf1))

## [1.0.8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.7...1.0.8) (2025-10-12)


### Bug Fixes

* restore parser command for help to the user about length of password ([6b16937](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6b16937faa4aebc090032c62c9445d0620531125))

## [1.0.7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.6...1.0.7) (2025-10-12)


### Bug Fixes

* restore generateDeviceSecret function ([142d563](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/142d5635725d3322d03304b757b76b624630733b))

## [1.0.6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.5...1.0.6) (2025-10-12)


### Bug Fixes

* delete unused function (generate password) ([1a08df6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1a08df62dbca54c75b8139b09244f09aa3e9d1d8))


### General maintenance

* rename package to "PROtect - UniBo" ([a260112](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a260112e2046f07f0cdb714c4795045999c72d47))

## [1.0.5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.4...1.0.5) (2025-10-12)


### Bug Fixes

* concatenation error ([163f452](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/163f452367481ad369b2f8e68b46784f34680370))

## [1.0.4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.3...1.0.4) (2025-10-12)


### Bug Fixes

* delete import about generate device secret ([3289050](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/32890507d045f5ba170edb3038c5e3377b8f1f44))
* remove tests on deleted function "generate device secret" ([5836a1e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5836a1ea5072c6daa98359a4b667d5c84fdba494))
* typos ([9414713](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9414713dbfac3271956cb7e1987e2055c2c09aca))


### General maintenance

* create README for artifact ([319cb69](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/319cb698eba9e01a726bd84fb3a88546061f3723))
* delete unused function ([411dc52](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/411dc52c27ba18e26282ca1fea977551b5a5edfd))
* delete wrong README ([69e1a8a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/69e1a8a56523999fcd61feba84a0bcbb685e81f9))
* release bump version 1.0.3 ([f88bcfc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f88bcfcdc20f7e771682ca79164e595bc92c1e20))
* temporary configuration to skip tests ([e7ef4ce](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e7ef4ce3e3ac133b2690c8fe180a55436479cf89))

## [1.0.3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.2...1.0.3) (2025-10-11)


### Bug Fixes

* title config ([765d98b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/765d98bcf7777bed6018e3df2b775b74c91a1e4a))


### General maintenance

* create README file ([a2abd64](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a2abd647e72590d93f977bda52d26ac133e0b9f4))

## [1.0.2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.1...1.0.2) (2025-10-11)


### Bug Fixes

* typo ([0cb4f33](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0cb4f3398acee695669dd0371ed531d0efb49532))

## [1.0.1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/compare/1.0.0...1.0.1) (2025-10-11)


### Bug Fixes

* missing comma ([d4cd7a9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d4cd7a98074d824ae4e88deb8016dc0b4021aefe))

## 1.0.0 (2025-10-11)


### Features

* add --all flag in argparse to retrieve all stored entries if wanted (conscious choice for better security) ([6fecac9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6fecac96ee700f9f18d723a316b35de0c318e78c))
* add add_entry method to insert new row of entries (all fields written) and refresh table with new data ([abe54e6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/abe54e6479d4781b29ab9e7e6c522466c7b9692b))
* add buttons for saving and deleting additions/modifications in tables ([c1fdd8f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c1fdd8f71cbb5bc2150d15ebac279deda039f84b))
* add buttons to create/cancel password ([8bfa74a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8bfa74ae4c15407f8679bf40b1435d59aec20699))
* add checkConfig function to verify presence of 'pm' schema ([c3b18b8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c3b18b85cb563c7e3b0a82769f21560e7a7c889b))
* add checkEntry function to verify if entry exists in the database ([f51eef6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f51eef626d1e2865ae9b2b56bb09d78aaf37ff30))
* add copy_password method to copy it to clipboard if required not showing plaintext (first refresh clipboard) + notify success ([e1b4ff3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e1b4ff31de29903599a9746e60b31778f17153d7))
* add edit_entry method to edit one or more fields in a selected row (write no new password if want to keep the same and the program automatically decrypts the old one through masterkey) ([772e3b9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/772e3b929bfb604c946445ac228f40954d01f428))
* add EditDialog for creating and editing entries. Create frame inside the table so entries are not glued to the edge. Define the entries. ([52025dc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/52025dcc5f6c1d166a97872eb95cc371628d26dd))
* add export_to_file method to create a .cvs file with all entries (plaintext) ([614dfbf](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/614dfbf143d0147d2e7277720e4fa2598c26faaa))
* add field validation (sitename, url and username necessary) when the user wants to collect an entry ([3efe270](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3efe270438e5f148a1b483c838094fd7241c920c))
* add function to compute master key from user password and salt for secure access ([05b58f2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/05b58f250c700ab7b479b7fb80ad739dae9b52d5))
* add function to let the user delete a configuration (it means loosing the SECRETS table configuration, hence no more access to data) ([ad521ad](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ad521ad5989b554a4fa3fb8201856c441e590b49))
* add function with mocked entries in the table ([a70d819](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a70d819137a6d949c3b036729a11a00e505e609d))
* add generate_password method in case the user wants a random password ([fcd1280](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fcd1280e4b4cd8d2862a7c0d588c0a6a0acbe546))
* add helper to detect username column in secrets table if exists ([aff024a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/aff024a3bdd19561a16e6e1333a3d131772df053))
* add import_from_file method to insert new entries in db from outside the application ([4b89992](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4b899920cff6c09d4c1224a50c2d34c17fe5090e))
* add lock_app which recalls "close" function to close db connections + exit app ([dffb94c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/dffb94c84b8a43e291272ae40e1b58691cf71f3f))
* add LoginController with database model and view bindings ([ec1ee47](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ec1ee4784f0c4f41c8396e013bca6b408d600b26))
* add LoginView and LoginController for user authentication ([9b80dd5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9b80dd5aada8ee07783d53ebaeb67034c069e78f))
* add LoginView class for user login and signup GUI ([74cc050](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/74cc050e52ab54c9f54c74c25d0ecfcbdd0eeca6))
* add password policy checks (min length 8 chars, uppercase, digit and special character) ([65c6f89](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/65c6f89a00b0ef4956a4fbb527d0cc2b1fe3c710))
* add show_password method to display password under user request in a pop-up box, only for 10s if the user forgets to hide it again and leaves the app open ([302ef5d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/302ef5d2af1694fd1c4451879459523c6747665e))
* adding AES256util.py script that can be used to encrypt/descrypt with AES-256 using pycryptodome library ([8c4a8a4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8c4a8a44124c968113afa94db129c376cde2118a))
* adding condition to verify if the DB is already configured ([837c11b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/837c11b44279c29dda1a0b5581b6997af367ad8b))
* adding master key computing function ([d087fce](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d087fcea8b132bcde8e2e4b80dbec69d4a487606))
* **app:** create main GUI window for application. Initialization of the window. Display Login when the app starts. ([df51b0f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/df51b0fe469b6de9065a52fc33c94349f083c89d))
* **app:** delete old widgets activated before jumping to a new screen making the frame empty ([d0653f5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d0653f5a9d7b886d6f815b547025d4d28e0b6e9f))
* **app:** display main application frame when successful login. Pass schema, mp and ds. If the user locks the vault, callback to login screen ([ba0ca57](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ba0ca57d73dbe123ed69e80b9819f6b43b08567c))
* **app:** show login window in cleared frame ([f36edd8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f36edd88481bf8852aa0a9a98fe8ebd58dcafa66))
* ask user master password again before adding entry to check identity. User must insert all fields, they are inserted in the DB and if successful it's refreshed to show the table with new values, otherwise error ([6f03c08](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6f03c080c97317562b2acaf093f70aca750b94a0))
* bind view callbacks to controller methods ([6e3cc49](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6e3cc49cfa53c8f5849c233daa32efeae2f3bb0a))
* **config:** clear existing table if any to insert the new configures PROtect.secrets. Notification of success or failure. ([36b90cc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/36b90cce7a5673babbc362eb10e1a50136a9b2cc))
* **config:** function to create tables, first check correct master password (and successful double check) ([b34df7b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b34df7b7133ff6ad55d70eaf67440c28f99f7b43))
* **configuration:** handles first-time configuration guiding the user. Ask for master password twice. If successful, create tables. ([f7c3ae4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f7c3ae4b636f21b2ceb59a3527573e4cce538628))
* copy function (for password) ([db59e52](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/db59e5231c39b03aaaa5097ccb823aa64e3b346e))
* creating the function that handles the insertion of a new password ([ad26939](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ad26939934ce42590431f8f3f439459d497bdd44))
* **db:** add get_db helper to connect to database with error handling ([cb4b79c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cb4b79cf737c923f0f3139ed1121d74242366bf4))
* **db:** function detect_schema to check which db already exists (PROtect or pm) so the GUI knows where to read/write data ([893ed9b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/893ed9b0612797e9d28e9457ef7980b698fe8d0b))
* delete function with mocked action of deleting ([6941a2e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6941a2e59ced51cadab728b2c014946918f52006))
* **demo:** add cladd MyGUI to make it wok in the demo-mode ([b2e8c00](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b2e8c00f7cebbc951e396d0b70b2e3aade0cc917))
* **demo:** add DemoController to add sample data for GUI view ([e1b5feb](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e1b5feb8d446eb484fa0ddb5752293ffe8cb50dd))
* **demo:** create main GUI window and callbacks to functions when buttons in GUI are pressed (still to define logic underneath) ([1bdb6c7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1bdb6c7f6fc5a305dbc3c61af67b78f23f333281))
* **demo:** empty entry fields when asked ([1665ec4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1665ec4804297d38bb717e855fc63d63117c2abd))
* **demo:** function to add a new entry (at the end refresh everything to see updated table) ([4190270](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4190270c8e7f12787725915dd2a4423a6b91d2f6))
* **demo:** function to copy password (mocked) ([f3cb108](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f3cb108ecc9ce30b11b91d2999592403e0ed28a8))
* **demo:** function to delete an entry when selected + refresh to show updated table ([a44f474](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a44f474c4ce6675b45d9b11eb63122826fbe97b9))
* **demo:** function to edit a selected entry ([64c3017](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/64c30171c7a29766f80a9700e9d543fb8d3a6ab8))
* **demo:** function to generate new random password (mocked) ([1bfc2f3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1bfc2f30ddbb94bf2cfba96ac8f83b1402c13d44))
* **demo:** function to let the user know a vault has been locked (mocked) ([0ed0af7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0ed0af7d6764b0fd6b4c7269bda2b14b59496da4))
* **demo:** function to show password (mocked) ([f67bc05](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f67bc0595f39086aad296aa6cd085306d64040e5))
* **demo:** import and export functionalities for data (mocked) ([aff5b82](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/aff5b82a9868983e65cb8ca23e8509a1fbc625bf))
* edit function mocking change of username ([6075c10](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6075c10506a9344bb8b43e4b813a7a234a552e09))
* empty schema before changin visualization with new required entries so things don't get mixed up ([596ef03](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/596ef032aab5e9bb43f9a1f75b0e141c37582120))
* function "row" indented in __init__ of EditDialog because it recalls parameters. Add label to each row on the left and a widget on the right. ([f712b45](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f712b453a84d87514d11cb10af4f57344bf0b678))
* function to copy password to clipboard to not show it plain on display. Check if pyperclip is installed (used to copy it). Check if a row has been selected to take its password. Ask master password again for identity. Decryption operation through correct Master Key + notification. Handle case of descrypt error. ([9aed738](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9aed738519e00f4b69dbd7b4a9ba5cd3b6b528af))
* function to delete an entry. Check a row is selected. Ask for master password first. Confirmation message for actual deletion. If everything correct entry deleted and refreshes modified schema ([b644f3b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b644f3b67658fdd340c5294372a2656dcc0dc61c))
* function to edit a selected row (stops if nothign selected), requires master password again. Conditions to keep existing password if not changes in a new one. Refresh to show the updated table. Error pop up if something goes wrong. ([aadefcc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/aadefcce979f2cad7ae0d641121712ddc4e3bd3b))
* function to export data ([40f2a95](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/40f2a957606aa47f310e9283f116b640ec422f59))
* function to export tables with entries specifying file name and path + error message if unsuccessful ([1efd924](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1efd9240085337a91576684e891107d352445f57))
* function to export to file ([68a313c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/68a313cdca9df286f5dd800e0a5898f31a7611ce))
* function to generate password (through GenDialog) ([6aa11ea](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6aa11ea466d7e0caa2f138e3fd416a237c55a015))
* function to hide sensitive data (password) ([5238fda](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5238fdaa1bea07fd2bfc272d18784904c12da505))
* function to import data with example mock ([1dcb867](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1dcb867672591b6c033716acce4ad8c8f135667e))
* function to import from file ([85adb4e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/85adb4e50713b50f30a7c82dfa88065321553505))
* function to import info in the table of the db and refreshes table with new values. Confirmation message + erro message if failed ([92349d9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/92349d935213271e41200c4ff29ff1c00e942b38))
* function to login handling possible mistakes ([05641e0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/05641e04b01a59802fbbe0d388168624dbd94bc4))
* function to manage signup and all possible situations and fails with warning messages ([4ba95b3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4ba95b37e36450a514534b5c2385efcdd9fcc76b))
* function to show plaintext password (through RevealDialog) for selected row if correct master password and successful decryption with master key, otherwise message error ([3ea67db](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3ea67db34933563558ebac80f11d82a36bd17541))
* function to signup the first time handling possible errors ([20c2956](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/20c29569324d9cae91874bae04bd6e65d66f9ad7))
* function to visualize the stored entries ([d6cf0e1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d6cf0e16c5c635b0bb08305e6403b1f39cf679f5))
* generate function for random password + case in which we want to use it to modofy a previous password + case in which we want to add as password for a new row of entries ([904a4cf](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/904a4cf1314906f542a60aa5fa1730b101903351))
* **GUI:** add main application loop. Added the App class and mainloop in the if __name__ == '__main__' block ([068b4ff](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/068b4ff471092f49b1ad311a5204cb7587e4a981))
* **GUI:** add main entry point to start password manager including a test modality ([b1495c9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b1495c94f78abc00a3c11de2d234b9ee0eb6f5df))
* **GUI:** authentication methods. read_secrets fethces the stored master_password hash and device secret and handles the case of not having rows in the "secrets" table when it still needs configuration ([1da8e29](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1da8e29c4939e6b0287f812a16d7fbe573e23919))
* **GUI:** setting up the GUI python file for a user-friendly interface ([1af450d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1af450dd30668ce91db1838ed94a953fc7155b63))
* implementing the "addEntry" function so that it first checks for the existence of an entry before adding it into the DB (linked to the "checkEntry" function) ([7987c89](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7987c89eefb40c989fc7dac153896bd8bba8672b))
* implementing the function to retrieve entries  ([5aa2833](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5aa2833e499836855ea16e5827fd2226d4d94a31))
* import base64 to encode AES-256 encrypted data ([27ee526](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/27ee526edd03694c097a98c4319efc1d89ac46b1))
* initialization of the password manager model managing rows of tuples as entries which are strings ([bd0866c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bd0866cceeed84f0af490e32317362ecc72e93df))
* initialize PasswordManagerController to handle GUI logic ([6afac7d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6afac7d92ee689c29ad09940ae28b3643c95836c))
* login verification (with flexibility for backward compatibility or incomplete records) and all possible situations ([b67fdfd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b67fdfdfd96fe7c8c9085109b713c735e86de317))
* **login:** add header label "Unlock Vault" to LoginFrame when opening the app ([2e217a1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2e217a16733f43b0788311c7f4e2de5fc382eb4b))
* **login:** add method to open a setup dialog and when it's compelte the login frame reacts accordingly ([1fe2336](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1fe23368f8b4e55b13f2612b15b89d40a7f8b879))
* **login:** error message to run configuration if after master password the schema does not exist. If the master password is correct access granted, if incorrect error message for wrong master password ([f6804d9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f6804d9750e78ca295686d400cc6e7a0e4739de3))
* method to add a new entry (the whole row) ([34b5fae](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/34b5fae83213f1bf348350b0403bbdf334e97063))
* method to delete an entry based on position index ([778f339](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/778f3396aab05c786ef2014d2392d025fe67c089))
* method to delete selected entry (recognition through ID) ([40f2860](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/40f2860f0d4b73fefcb36619524b40971e574b7e))
* method to edit an entry based on position index ([e6ab47d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e6ab47d08596c3d3aa267a545024a160fa7476cc))
* method to generate random password with requirements (mixed chars, default length 12 if not specified) ([6027667](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/602766725ab7dafbe83015d44d80342a77e00c17))
* mock data entries in the table for demonstration ([92c2c2a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/92c2c2ad3b8bb8811e2da38f511d045ba7d9c60e))
* **model:** add get_password function to retrieve an encrypted password (which gets decrypted) for a selected entry ([53d5766](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/53d5766c4870d10bafacb4608d2b26bd08d4fe1f))
* **model:** closing cursor and db connection ([4e96088](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4e960884787df89e21e4a36b442faab753e556a6))
* **model:** create db PROtect and tables for entries and secrets to compute Master Key if they don't exist (first initialization) ([d799393](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d79939384a1d4c70ae693300f791cf9bcd7991bf))
* **model:** establishing real connection with db ([74af016](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/74af016ccb90e46bf6a7a5f24b93c5832655e2f1))
* **password:** add hide method to mask password in the UI with dots ([29eef3a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/29eef3af0847811e2ea9682ebd24cc859b5c285f))
* prefill entry fields to make it smoother for the user to add/modify info and Enter key bound to confirmation in EditDialog ([032851c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/032851c8de752e35bbd5fc6bf17491f5fc936484))
* remove any text from the password entry field after an operation is done ([1dbcd88](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1dbcd886b7420a3274d38b80d9d7a32e3937b5cf))
* **security:** add PromptPassword dialog for master password input ([b8d3759](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b8d3759c18ab118f526e899c9df5a70ff812171d))
* **security:** requests the master password to the user, waits for the input and checks if the insertion corresponds to the real master password through verify_master ([ecc02a7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ecc02a711454d9de2335442ba2f06627f9ba4daa))
* **setup:** add after_setup callback to reload schema if it worked and notify user ([3400780](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/340078042b2d4a759b20fb399bba40886779ae68))
* **setup:** add SetupDialog window so that a new widnow pops up dedicated to setup ([d4524db](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d4524db4e7d448930348475d2fcf403b70aa9844))
* show function to show password temporarily if user asks ([ddea013](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ddea0137b8bff2a33a804b9d0ad9f53a05e043a4))
* **UI:** add lock method with confirmation dialog (yes/no), proceedes only if yes ([8c1bf78](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8c1bf78d7f82b0910c2f5f607cdbe68e710b4a8d))
* **UI:** build main header bar for the password manager with lock/export/import buttons ([8a5d619](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8a5d619092d54ad50e00cedd4f61c9a7089852db))
* **UI:** create an horizontal toolbar at the top of the application main frame with buttons to perform actions. Separators are used to gather buttons as groups ([77c9f23](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/77c9f231ed979147e57bc202a3ddc95700aeea62))
* **UI:** create table with treeview to display entries. Set headers for columns and formatting (width, text...). We bind double click on rows as copy password to clipboard. The cache contains the whole information including encrypted password that is not to be shown on display ([4cf9f7a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4cf9f7af67cd1f15e01bcf460e366f3973b8e518))
* **UI:** refresh function to repopulate the password table in case something changes (add/edit/delete) ([d69175f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d69175f610c664095b7777a756bd8bb924451388))
* **UI:** select rows and handles the case in which nothing is selected ([b6f3835](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b6f3835e7ee9225ab92ddf133484ed2b5cfd9f1e))
* **view:** add "dumb" GUi interface letting the controller handle actions (on_sth will be called by the controller as commands, so we don't define their behavior inside the VIEW) ([445c132](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/445c132e66717bb5ac9fb71f16de90e6b1fd22de))
* **view:** add "dumb" toolbar buttons (with callable controller functions) ([2d55dc9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2d55dc9bca5f7c66e4d064ed09fe78405a1aff66))
* **view:** add main buttons and header to GUI visualization ([be21b5b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/be21b5b6cd8cfdb74c464a2c3729d9e28103c719))
* **view:** add method to reset the Treeview, only manipulates how data is shown ([bb1a6cf](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bb1a6cf22e1d1b3843b57a34d5179f849cf73424))
* **view:** method to define what to put in table rows (and format str). First delete older data if present and displays new one ([cac0e42](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cac0e42d31983c7acf80e237054e7269cf1b2c26))
* **view:** method to format how to show each kind of possible message to user ([6295b45](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6295b456b6a05ec9db524c1c8f61dbc3b5aab97a))
* **view:** method to select the row to get the password the user wants (+ handle case in which nothing is selected) ([f3bba31](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f3bba31aa2a5e82946358eeceb38e17952015b5f))
* **view:** setting up table visualization in GUI (no shown password because sensitive data) ([c8521be](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c8521be83a5cd89f49815a1d4fcfe041a04806e2))
* window used when plaintext password requested, displayed for ten seconds (framed) in case the user forgets to hide it ([87042da](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/87042da82c0c0cdb51757ed14be2194827cb8efd))


### Dependency updates

* **deps:** setting up python version file ([8c2f126](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8c2f1260b85240b550f8c072f8b79a2042fce2ec))


### Bug Fixes

* "password" instead of "passw" for the variable name because otherwise the function from mysql.connector does not recognize a parameter called passw ([7849929](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7849929ff829fe73480e1c66f4174db50c8dcdc0))
* add column for password in GUI visualization ([1a5ae20](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1a5ae202b9e9efc04aaca36ef805286cf9f508f7))
* add column for password where needed ([0247c30](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0247c30884906c9c58a33815748aefc2d2f95bae))
* add parameter for password ([a90a6a4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a90a6a44ac42dbe77896da26add0f3cec429578b))
* add parameter for password ([05ac4b8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/05ac4b8c99450e4d2dbda460ed9f0fe0b0427277))
* add parameter into the function to print the exception ([5efcf64](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5efcf64ef80222bbed249ec8ea2761d942351271))
* adding assertion that states the schema exists ([07d087d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/07d087d3495e57c0c2271348d038ca8b92996d24))
* addition of code files (about the configuration) into "artifact" repository ([4e869d6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4e869d60238422d8424ac9affcbedaf4fce517d7))
* adjust "view" variable definition ([9125d52](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9125d52b473712eea3c120e5bedafeed5bb7e34d))
* adjust characteristics of copy function ([0f2ea6c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0f2ea6ccbf7e4fc62c6cb7c58426f3975fbc7d5d))
* adjust function injecting real controller to interact with the view ([554972d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/554972da15f09822aea9c1329050cce2bbaf2530))
* adjust import from VIEW ([f2c2197](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f2c21978859f6eaa432afe3e650c2cfa1d49cc6d))
* adjust import issue because files in the same folder ([9f78df6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9f78df622d72ac76fd211ef3ad3739190323d6a4))
* adjust indentation so that variable calls work properly ([033b7d9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/033b7d936d511ffbf464b338735cbb32be039d29))
* adjust reference to class in view file ([ccc3f9f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ccc3f9f304a51967412cba719f8073055d592492))
* adjusting import specifications from config.py ([f0b8069](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f0b80695110491812140c34b01ab3e0d5a1df69a))
* adjusting indentations in config.py file in VSC format ([ecd8388](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ecd8388cc0397114462a4cd06f8abb0a2f54cfa7))
* adjusting indentations in dbconfig.py file in VSC format ([457b0bc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/457b0bc121b62d27621a1d5261dcaf21dbb02c7c))
* adjusting naming conventions to variables ([47ad8da](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/47ad8daae83e21906a5c38a61ad4953f88dc193d))
* adjusting requirements.txt file based on the use of poetry which already contains dependencies ([eb12437](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/eb12437c88aa580e84da9e779199e809f9fa79fb))
* alignment of return in the dbconfig() function ([bfadc96](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bfadc96a92ddc84abf8b538b62c2f2a658065993))
* alignment of the except block ([b540eda](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b540eda8ffbc1df81aa7f10a2c0dd16df79ad29c))
* brackets error at line 29, 'entries' instead of "entries" ([e5d4215](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e5d42159298a9b81ac34fa17923bb2e9dfd44b72))
* changing folder name from "code" to "project" to avoid conflicts with the built-in python lib ([38469df](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/38469dfa2e9fbd9f5945b1de51c2acac5765f28c))
* changing name of the variable at line 10 from "pass" to "passw" otherwise not valid ([bd70e36](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bd70e367d3ad731061a2987c2e7a66b99a7726f4))
* changing naming convention from "code" to "project" ([d011076](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d011076b729c966f143f4c08f823ea72a9e8e887))
* changing version in tool.poetry from 1.0.0 to 0.1.0  ([0aad60d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0aad60de5fac7d73f6884b6b3579f392ceb6f496))
* code repeated twice (keep the shortest and most efficient version) ([622af4c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/622af4c8008c8359070f4faffdfb5d0bbd0d4a82))
* correct import of AES256util ([40f3a5f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/40f3a5f28f6ba93e0780ab3556db45016cfabe8b))
* correct name for folder tests/ ([37ab5fc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/37ab5fc691b647620251d3fd269d711d2e5882b0))
* correct name of the variable to recall ([b536aa6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b536aa6fe7d1e73f1ab90f9271553245ccdb8d3e))
* correcting indentations in VSC format ([6e7e684](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6e7e684871b12f8e5b447a4fff213dee6e53782d))
* delete .yml file (attempt to publish on TestPyPi ([1a54c32](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1a54c329aec21b93cb94619926fac26258ae3a70))
* delete "=" to not break the mock's assertion method (syntax mistake) ([ed69418](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ed69418a948dc093e3c8ef1fe27d9650b9040419))
* delete closed connection because we need it always open while interacting with the db ([31eef0b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/31eef0b2cfeafe3c92c0ba86b526e372a12e8a94))
* delete empty test file ([21a719f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/21a719fe84ff86e53ba7bb77d2ed6ca41a50e17d))
* delete password column in the GUI because we don't want to dispaly it for security purposes even if masked (security problem: counting chars) ([a253d1f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a253d1f10e6cffa04258154ef8c0ecd73fb515a3))
* delete unused function (generate) from the possible commands to pass in the CLI ([b5c3efe](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b5c3efeec4dd95760f7ab83d601c1be5fa5d3cb3))
* deleting a parameter ([102124d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/102124ddc04fc5fed92f20bfd254d32847f7c30e))
* deletion of python dependency specification ([80f9558](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/80f9558de9f5547ff4c6c96349dc203c20eda100))
* error in defining the function into the variable ([7ba363f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7ba363f4100a7672ab1a7196da4b9482c23c5003))
* expected index in the square brackets (was missing). Indicate the password must says the same if not specified otherwise ([3e0a128](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3e0a128e170315ee516df49b82a98b4f0fb583a2))
* **export:** prevent plaintext password leaks by exporting only encrypted values ([81061c8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/81061c80c9f201b45c859b7ad4935003ecfda3f9))
* file name ([a4b44b6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a4b44b6a0ad2213c877b406451ca26cbfcf48bb5))
* file path ([9a231c4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9a231c44832a687ecae990acb56eec86a908f866))
* fixing all indentations ([340d18b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/340d18bfe8a715d193950a19dcf8ac720a5e0781))
* fixing check.yml ([4676862](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4676862e08625bcf1f5b2e16a413e4138b87e341))
* importing config.py specifying the different directory ("code") ([2816b54](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2816b54ff64bf027c9e4d5506ec98e3307a26631))
* indentation ([77ae3ca](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/77ae3ca2577a8cfe9e96ea66b55e226785974731))
* indentation error ([8ec1a6b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8ec1a6bb92e25350699e054ab982c89574f515b9))
* indentation error ([b91e9a4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b91e9a42e90dce2a5364efaf510013dbdb1a2082))
* installation of dependencies (no poetry) ([24a2c38](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/24a2c384c138f2c0f1d1480b4deacac744a27176))
* just deleting a useless space ([878cb8a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/878cb8ae9ef63dec19ea476ce7abefc2806a2ad1))
* logical mistake for double checking the chosen master password ([1f661b8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1f661b88826b0ff1a5a420ae9f468aab70baa0e8))
* managing login and signup based on new column "user" in "secrets" table ([918633e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/918633e2d10ff6e25a131415f35c1ae09ca0145f))
* missing parentheses ([9b54f53](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9b54f5381c9adb131b3358b91acd5deb7129289b))
* more specific about what to recognize as a package ([563f28a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/563f28a539b02427e5c5b2a2703ae70bc8d01ff5))
* name of some variables ([1bcae80](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1bcae80ca82b9f9b1ccc491ad6fd6401fbfcf0d2))
* naming convention for AES256 encryption ([2b6db4a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2b6db4a62ccd49ad3490f26a588c17aa72995ada))
* naming convention for mocking db connection ([6426e0d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6426e0da56d1b3f0c21ee6cbf253a39c775a5973))
* naming convention for the DB ([e1bdfc7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e1bdfc7ab599f97625dfb962e0a7c9bb43c5e14f))
* naming convention in import Crypto.Random ([c445c86](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c445c86c66067f0a18cea903a59fb0863ccc59eb))
* naming convention of the variable ([5464ac2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5464ac2c0948f86fe82e6daac17362672d67f614))
* naming conventions for db and mp ([9c51a74](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9c51a743b08d2415d7bd8a3984910b519a1c7ada))
* naming conventions in import Crypto.Hash ([ff085b1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ff085b14b647a3f78b41e252ebd6c171996481f9))
* parentheses to call methods ([2a6c9a8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2a6c9a83836924f4c1f81c880976215b26e8f80e))
* reference error to "add" code file ([4a96104](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4a961041f13135075deedffe4950911aec0cfd6a))
* reference to "generate" code file ([bd1e872](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bd1e8727b3291bf2d0bb58aa633ffc0a5f94c0df))
* reference to "retrieve" code file ([ece68fd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ece68fddf32f00f4e6713a8df184f8bf2a7794d4))
* remove "root" parameter (it was a repetition of "self") + pass on show_message function (needs to be revised) ([0df7844](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0df78447a5a6cba7b66404c22866218c8682e2c1))
* remove deleted function for the user (generate password) ([0b35f85](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0b35f85f6b63c5b271e089865fdcebe42616f50d))
* remove unused import (pyperclip is already brought by retrieve.py) ([f94f25d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f94f25db3afcbbb664c4588f59e8a28b9bfc851f))
* remove unused import for pytest ([7681142](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/768114200169033936a9f3ae2c91be4702542fd0))
* remove useless imports ([0f8fec1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0f8fec1d6b9113e5d2de5322893ac9732a44efd0))
* removing import of unaccessed OS library ([1ffef8e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1ffef8ee880a392f3646f2eaa181cac09da28d41))
* removing the check on password on secodn try because already included in another test code ([b34b40b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b34b40be1e99c788ff8e953b23f14dc67d946f6b))
* removing unused imports + adjusting import errors ([b135303](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b1353032889952116a04ce5cb6e75dc0b3a6304b))
* removing useless parameter "master" ([79bea95](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/79bea954f4ab5b9b18e0eb278a947a916db62ccd))
* restore __init__ in ui package ([de396c9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/de396c95545f84556099e2970b2b73a6911cf216))
* restore .gitignore file ([a469f62](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a469f62e327ce8ce569ab65dd983d297b32849c4))
* restore gitattributes file ([3cf558d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3cf558df64a90ab5897d2030e0bb5d57592c679f))
* restore MIT license ([d707ca5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d707ca55df75f50703700fe7beaf0f692dd63b00))
* restore python version file ([8d934aa](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8d934aa1877c4c3d54131550ea8e418ae57fd68b))
* revising import to correctly call the function ([0bc40a6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0bc40a6603079e8138081e5b1924da9b8c964a7f))
* rewriting the import of "dbconfig.py" specifying the folder to see if the tests work in this way ([e6e1a05](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e6e1a05051153bb97eef1086877a71c1ff943eaa))
* right specification of the imports  ([09f9a1c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/09f9a1c092a79a9383609dcbaef0adfe7a14968d))
* syntax error in SQL for encrypting password fields ([93eb0e7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/93eb0e78d273f1b2d668551056271d815ed87d4c))
* syntax errors in the mock's assertion method ([d043f1c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d043f1cdad3dca400608d29bd4cb01cb4b2a4524))
* the database already exists, so the check needs to return "True" and not "False" ([aa24b26](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/aa24b26745b1fbdbacd66ffcfbffdfb8395bfaa3))
* the DB should be first initialized if the return is outside the "except", otherwise db is always returned even when undefined and we get an UnboundLocalError ([2c7b818](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2c7b818195d6eeb424c159b3464770badb91f57d))
* try to run tests ([ee3ba52](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ee3ba524202c86bc83a41cc0daa37ce41a9f1d9f))
* try to run tests ([93f21bd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/93f21bdd219aa04aa12a992440d107bbd9ac6cb7))
* try to run tests ([446b702](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/446b7028ef0f3009a5c85645185dedf3e6b31460))
* typing error for the parentheses ([ddacafa](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ddacafa9754b14d6f7b04e89837f645801b1210c))
* typing error in MagickMock (should be MagicMock) ([9fd986f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9fd986fa319b23828d3ef6f2d013edb0a11165d3))
* typing error in the computation of the master key ([6aee37f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6aee37fa7a003e545714c0a2a28e5873d0957088))
* typing errors (dots instead of commas) ([68e4ada](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/68e4adaf534eefbbfd454082b05afaa7d582a7ec))
* typing mistake in the while loop ([d89bc39](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d89bc39d774f70d72e4b4b465a73c9524ba97642))
* typo ([3112f78](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3112f78125fbf5114b3781810281b75679b6548d))
* typo ([1a4d2c2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1a4d2c2b230a1858f74d80c16fbcdb48bf0c36d9))
* typo ([cc2d020](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cc2d020140941a03e9906d68008b743a2f5d979a))
* typo ([ff124de](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ff124def6f75bd2d93316e06da8abf68020d01d1))
* typo and anchor errors ([9976c56](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9976c5609dbe55de28f8dbca227a4a7950087d43))
* typo error ([22e9ca6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/22e9ca6cb25649665fce38565b3fa8f9713e09c9))
* unused variable res for executing queries ([e3c3ba9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e3c3ba968ce2c087631ed68cbfe8bb793c571d4b))
* uppercase error for Callable ([58b3704](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/58b3704c76d28cd667369a5f11732f38b3e0d991))


### Documentation

* adding message to notify the user the db is beeing configured ([85638d2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/85638d24631cb28e07d7179142c729d0c361ef77))
* clarify user-facing message wording (username instead of login for the user) ([b92d5d9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b92d5d99562583a01c37273af219192ae48825fd))
* disclaimer to the user to let him learn about the master password ([b3d71bf](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b3d71bfb39b0b61ea28149ced070cd7be575969b))


### Tests

* add pytest fixture for DB mocking ([b985b55](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b985b55baef77f73f45a940994474791e277febd))
* adding a combined test for both length and characters in the device secret ([01abb30](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/01abb308c8afd91acf01a77f42a404edeca5b0b4))
* adding code file to test the configuration of the database (dbconfig.py) ([0ac027b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0ac027bc44b7fe62c40e7534fefa66ea24f744ac))
* adding test for checkConfigu from config.py. Used to verify whether the DB exists ([46ab5ca](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/46ab5ca28df121b1adc722aac83eeb33282ef751))
* check DB calls ([8b93aaf](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8b93aafd48a03cfba85ceec9c665a4b480259e93))
* check password hash inserted ([ea62522](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ea62522baaefea268a84d6d6bac32c6b66b67e86))
* checking the allowed characters and correct digit of them ([ebd4a70](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ebd4a709311c1c85c15cae6bc235e96a9ffe7dbd))
* checking the generation of the device secret with the default length of 10 random chars ([e23d747](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e23d7477cd3a3aa4fb84afccddf799d5e7e5f321))
* checks and already existing configuration, so it recognizes it and does nothing more + warning message ([8b8a115](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8b8a115950b11368fd4e534578f834747f33da64))
* checks the function is called exactly once with specific arguments ([2d64773](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2d64773d30f2067752b8edff4b775dfdaaad07eb))
* checks whether randmoness works or it's broken verifying whether the generated values are for the majority unique ([14fdcc0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/14fdcc096e531a52cdb97232c49c2a518faf4903))
* commit and close called to check whether commit for changes and close to properly close the DB connection are called properly and only once ([fa78c5e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fa78c5edd8326feebfc390837581b1e64f3b4ffd))
* creating the file to test the configuration logic ([d6795f2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d6795f24fdd22f1fd8201968d125357a09ebca70))
* error message whether the DB maybe already exists (error while DB creation) ([d7aa879](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d7aa8797732c9d1b026572157a30682207d281f7))
* handling failure of the configuration of the DB ([4213bca](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4213bca376b1538433ba856044944d0edf677b5e))
* mocking getpass to simulate matching passwords ON SECOND TRY ([a21be66](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a21be662e22ca9e962d9199862c4a5b84eb58fb6))
* mocking the DB connection to check and control the behavior of the dbconfig() function ([76ee632](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/76ee63270e5cb2f54ced974c0257724e01af275d))
* mocking the elements we just want to simulate ([f9058b0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f9058b0bf53540bc69e97dd692ca5b4e2b69a808))
* patch to simulate the user inserting the password two times correctly without having to wait for a real user input, and it forces the device secret to always be "SECRET" so that the test can be predictable and does not rely on random values ([1ee3917](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1ee3917fb64947d972a47dc73a06b65093d0b5a9))
* printing the green output stating success ([8ad8ffd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8ad8ffd3d0999c98eff830dd2fa4a2f90ed6e980))
* scenario in which the DB does not exist and needs to be configured ([61daa7b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/61daa7b209ef1d8d83fe869b10f3f17da39545ed))
* setting up the environment to check the failure scenario (non already existing DB) ([1b8fd76](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1b8fd76e59bb39b19cfa3f2bea14cf01cc74b150))
* simulate exception on CREATE DATABASE query ([6c86a99](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6c86a996f9529fece5fd9877c36c7083312ac62b))
* test for checkConfig in the case the schema exists ([fa52f0d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fa52f0d63c9f5c44cd5f202b53df15dd9ec6e25e))
* test for checkConfig in the case the schema is missing and so nothing can be displayed ([4ecf887](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4ecf88750875e1463637533a4c6d1bed8438ed1e))
* testing the generation of the device secret with a length different from the default one put in the function ([55bbb9b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/55bbb9beb2d4eae494587c20a37700904686b39b))


### Build and continuous integration

* added permissions + added python versions and dependencies installation ([29ebcec](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/29ebcecda137ed0cd655305cc2b151ceadd1911d))
* changed configuration for dry release ([915c73c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/915c73cd341aa365d48fef7e89502ec796f7e966))
* **deps:** add check.yml for CI workflow ([73629bf](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/73629bf09409a3ba20513689ef0c58f1217aebd7))
* **deps:** create deploy.yml for automating release under some conditions  ([f59a47c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f59a47cab468ee1ab8882560534bd4de09e000f6))
* exclude devtools/ from packaging ([4e52625](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4e526254a92cccdec656e4416b85418d655995b0))
* remove poetry.lock to simplify build configuration and dependencies specification ([3e38493](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3e38493ee72900554a02e5f0bbfc60d582200948))
* remove poetry.toml to simplify build configuration and dependencies specification ([802f949](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/802f9498feacfec98caf624f73a02f0ea84f5f0d))
* remove pyproject.toml to simplify build configuration and dependencies specification ([b680620](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b68062099471cf38a3ba6e15807b518a354ace3d))
* reorganize workflows under .github/workflows ([c8244a5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c8244a5c409645a8abe61021fb59d5670c1aec72))
* setup production and test configuration through environment variables when launching protect GUI ([00ab01b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/00ab01b73f6bbeb3e13558dcbe06514ac24fe345))


### General maintenance

* add __init__.py configuration inside tests ([b2cc9c9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b2cc9c9d96f12dc164923d50b967b6463b72843d))
* add __init__.py file to make the VIEW package importable ([4f658ac](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4f658ac72b776198b02681516b6f4dec02f0d2e3))
* add __init__.py to make CONTROLLER an importable package ([f0213ff](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f0213ff4f3d617119c8e81d2bc1ad590c639c480))
* add __init__.py to make devtools/ a package ([cfa1b5b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/cfa1b5b44615b661cbf815685c01a881fc179ea9))
* add __init__.py to make MODEL an importable package ([9f97daa](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9f97daa94e59851174e2748ef1f9be27618a8bc5))
* add .py extension to test_config file ([dbc2758](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/dbc2758d18e31a62c16a1f57096b4f21f8e86550))
* add demo file to interactively test the GUI (not a test kind of file!) ([558f8d5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/558f8d5c730faaef12ed824c4f0325aaff17cbf8))
* add folder to exclude from release ([478fd2c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/478fd2c2e643f4104ef99ad55a6dd59372c280e6))
* add import for correct reference to PasswordManagerView() ([e3d218e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e3d218ec41d63b7625fb3df73cb94291e03e4d3f))
* add imports ([2e917af](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2e917af9156dc27a94b072e5bafde3e3cfea3077))
* add permissions for release (write mode) ([1e2d3af](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1e2d3afcba6b0b37eb9c723d8e08dde6f38057ac))
* add permissions for release (write mode) ([bbcc289](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bbcc2895125b707a23e5a0b666f5cec7e30c309d))
* add release branch ([489c3e2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/489c3e22d507d65084a24189f3de55d961f9f027))
* add useful imports ([924e8e1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/924e8e16aa5366ed736d49c692921b7ce330484a))
* adding all possible options for the user based on new functionalities ([8e52676](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8e52676a27a86f9f3eedf6819e9c6a447d911e6e))
* adding description for the use of argparse ([3f28145](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3f281456f12dcb17bdb8e078c8dccbb4fc884190))
* adding import of pytest while deleting unittest (maintaining only unittest.mock) ([2d1a4d5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2d1a4d501e4644c0540708acd0b42f867e5d66a4))
* Adding MIT License ([389757e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/389757eaf0596d28e1dfbb9d5f541be9751d8978))
* changing subtitle for the specific test to be more precise ([0d12325](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0d12325a975cd7c3ad1de49941159d97171465dc))
* completing mypy configuration ([7517bf2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7517bf218fc8f3fb678dbb33b8c21af5b9d3f865))
* **config:** ensure DB closes and config runs only when executed directly ([76e6877](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/76e6877bb01c6a2fd95edca668b4f578603009e2))
* Create __init__.py ([3f7d369](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3f7d3697031aca444e3f36a0a477565bafe31315))
* Create MANIFEST.in ([0445065](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0445065b804b26d8bb86fdebbc24a48585cb54c9))
* create requirements-dev.txt ([ea2993e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ea2993ef9bd0bb12f7960f5a53be7ac2e6f2b902))
* create retrieve.py ([9aadfb7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9aadfb712d22ca5df33df207a93ce15095fb054e))
* creating .gitattributes file  ([f9e0ee5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f9e0ee5a7b4e00a0141952f965e2fd8e9166c349))
* creating .gitignore file ([caaca03](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/caaca0340f83a2871665b36cc8e97501d2f50a24))
* Creating a "code" folder and moving config.py file into it ([60fd80d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/60fd80d41616431be1c95de5c96ba260a6fee182))
* creating test_add.py file ([1c84395](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1c84395cafe6a914349a14c07d126ba219ad6fa3))
* creating the add.py file ([7515501](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7515501b29928b9ebe923e3c9a9a85ffe1829e5b))
* creation of mypy configuration file ([b7fd0cc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b7fd0ccadb55160c32db7f2297e4d16973a22ef0))
* Creation of poetry.lock file ([a6f9b1a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a6f9b1a815cefd1bd395fca9b608fc54dd1c25bb))
* define the content of the row (without specifying frame everytime because already set in function "row") ([c4dbdfc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c4dbdfcfda1e99e449eea4108008414c9b3d8e0b))
* defining entry point for the application GUI ([1add23d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1add23d23f1d27566b7f75ab7d09e68ec482ce3d))
* delete old mocked methods because now real controller behavior ([06cd1fd](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/06cd1fdad6087e3630d2f5dada93e1f7f5b2a2c5))
* delete python version to see if run tests works (GHA) ([77dfa5a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/77dfa5a7960ca8e76fcb81056852a5e08a56c915))
* Delete requirements-dev.txt since we use Poetry ([4d9c8c9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4d9c8c9f2cbaf814f4e23716f48c97b8b954d2a8))
* delete useless function since now we have initialization of schemas for entry strings ([976e5ab](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/976e5ab85f20f2f0d33c83406bf894dca9286117))
* deleting function to generate password (removed feature) ([5cbe809](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5cbe80992ab75c41310ff4c61ed90ff0b9423d65))
* **demo:** move demo.py into devtools/ to (because it is only for test purposes, so we won't ship it to the users by ignoring devtools/ at release) ([44daeee](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/44daeeeda64bb758afa1f1d1a6df2c65a7a3bdd1))
* explaining the error message in the print statement better ([ed83aa6](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ed83aa6e3f9ef792d8a7c7ee262b83bccc6cd674))
* explanation of __init__.py usefulness ([a8a68f4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a8a68f4a20ce0cfba258190c207a28cbac9732dd))
* format for rows and avoid repetitions ([9f88585](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9f885850f111b9a18c9a368c68e3f11c746cf898))
* **generate:** delete generate.py and correlated functions to remove the functionality allowing the user to generate a random password to end up with a simpler and shorter code (we want the user to always choose the password) ([bda244b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bda244bc81dfcd08201e4822b00639106b6d43af))
* **GUI:** remove deprecated GUI file ([ee027c5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ee027c591b4b84c2fb80930a950a4d2799153336))
* handle imports ([ab951c0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ab951c0f9d854a1bb8911aaf2da973bb78f89a78))
* implement delete function ([7453ec9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7453ec93c814b82f3b81fa22ac7dadc5e7023f8a))
* import dbconfig from utils.dbconfig ([c2e7b39](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c2e7b3930a44f98e3e709d5cd1b050e8b47d91f9))
* import essential functions from the Crypto.Protocol.KDF, Crypto.hash, and Crypto.random modules ([29b0a60](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/29b0a6072c386e6877b2b5af152337ca833e7649))
* import getpass from getpass ([3c5c830](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3c5c8303f6fab188ad868f69e9e02aab4705d7d2))
* import libraries ([c4b2fd0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c4b2fd0f8c2eb482097e022c11bd72eb97196193))
* import libraries (ttkbootstrap and tkinter to modify GUI graphically) ([7eb0797](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7eb079742515af0a42fbad1cf83d28cfd429667a))
* import modules necessary for decryption ([8a65a8d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8a65a8d72533f259cd96ab8f11a4df9602166133))
* import of ttkbootstrap library ([455ac4e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/455ac4e1c953c3bff0e9734b246844036fa693a9))
* import printc, Console, and Table ([65704e7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/65704e780f9b51fd790bca4d32bb15581e31f239))
* import pyperclip ([f598360](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f598360fe92060fe71207b82a8137cb294ae2a70))
* import the utils.aesutil module  ([b6999a7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b6999a742ac300c14bfa097f5ac576e94777131c))
* importing "computeMasterKey" to being able to compute the mk ([df4394a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/df4394aadb29287e38628d4dbb91dcb6a66fc5a9))
* importing "string" useful for master password security policies ([985059c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/985059cf77f5b94668154bcd2af40f519315cd02))
* importing console functionality from rich library ([0fcd69f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0fcd69f7ab5559ed37aac9152af0a1bdccd3620d))
* importing dbconfig ([0eaf511](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0eaf511c2389c75f635f843a775082a7627d60f2))
* importing getpass ([bd12c1d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/bd12c1df166adcd44bfe4c8d6f8e62fa0032e583))
* importing hashlib ([96d0821](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/96d082116846ef7f0abac0752bf3c4e40d67c96a))
* importing libraries for testing in test_config ([18b3ad5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/18b3ad5106de30646c5fc9607a80027bfcce0e81))
* importing needed libraries and methods ([4427ba7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4427ba70ffbb60ce5beaa4ec36d9fc2a03726035))
* importing OS library ([5ef7665](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5ef7665301ac7226cf72354c5ac276359b0ede0c))
* importing print functionality from rich library ([1bf3a0b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1bf3a0bb55eec09d0682af9bdcc73e381650cf94))
* importing printc from rich library ([5f6f6ab](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5f6f6ab73c2a7958e1f762c7a4e4894f22c9ccd1))
* importing random ([0b1ae27](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0b1ae2791547c2022b6669bf4ccaf4b6f1ea60d3))
* importing string ([04f5184](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/04f51846fdd54eb9647562b2234bcd90844057a3))
* imports for the login view ([05131aa](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/05131aa558e1786e94b5da37a73e2f7928826db2))
* lines before tests to specify the function we work on ([58373b3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/58373b314b2fd9cb98fa9136afef523b1a663ace))
* making view definition a comment because not needed now ([83b277f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/83b277fd6383d806efd68e77ca066994b1e98888))
* manage imports of methods and libraries ([3c0c847](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3c0c84783734ca7852e0beba9688a6112b1635be))
* managing all useful imports (python libraries, third parties, ttkbootstrap, tkinter for GUI) ([0a43dfb](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0a43dfb67cf6810436dbb1c5eb2ea97ae47be7f7))
* merge remote-tracking branch 'origin/main' ([8ba9304](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8ba9304f69d6e27e006494c3c49bf59ed2acebc7))
* Moving dbconfig.py into /code directory ([1889472](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1889472358efea246307eabe92bb400fbe04214b))
* removing generate call (because no longer used feature) ([d831ee9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/d831ee9895a6808951ba90af9adc9159873f96e3))
* removing unused "generate" function for random passwords ([2814528](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/281452833ca25355cb4c26163b6fddac9e9cb6c0))
* removing unused imports ([35fbbc5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/35fbbc5065559ae651781c6af39f10c9c8d957f3))
* restore requirements.txt by means of "git checkout c29f4cfd7b85e5a9551f2982cad6d0465dcd21b2 -- requirements.txt" to stop the use of Poetry ([7a5263f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7a5263fe0c50f882d2763375348ab2343a66fd43))
* setting up empty __init__.py to let Python and Pylance recognize "code" as a package ([ccef22e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ccef22e09cd2f21e7984cc9bac450f7dd918658d))
* setting up poetry.toml file ([c15bbbc](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c15bbbc144306b3af0db84cea291798d897d217a))
* setting up pyproject.toml ([9134cb2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9134cb200678e522d8f2545291b53426d5afc5d8))
* setting up requirements-dev.txt file ([39a77aa](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/39a77aa843e274328f662f9d47ba8b1b00b9d946))
* setting up requirements.txt file ([c29f4cf](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c29f4cfd7b85e5a9551f2982cad6d0465dcd21b2))
* update path ([7fe464e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7fe464e27fd32621ab0ff28cb283339f7274bb1c))
* update path ([448c198](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/448c198f9585a085e096b26de3f7ae90d6de7f56))
* update requirements.txt with new dependencies ([92c177e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/92c177e7de72dc6eb44fb0db0f0a845f4235f7e7))
* update secrets table to allow multiple user accounts in the app ([0162bf1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0162bf1c73c19d0dfa0bb2efa2e4f97f4e2a0819))


### Style improvements

* add description of CRUD operations to logically separate pieces of code ([4675b3a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4675b3aab56c15271bb52f54a5de22c3927ad8e5))
* add description of next set of fucntions to logically separate pieces of code ([5c3d4b3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5c3d4b3f4fee81a0992f5d018b85cf307d6ce8c2))
* add description of next set of functions to logically separate pieces of code ([8d82d24](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8d82d24ed01bdb2271db77be39fc1ae30df1c3a1))
* changing positions of functions for readability ([0b207c0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/0b207c0ce7572ba534a11e1f0b10161981c11d3e))
* **CLI:** improve output formatting with printc ([5a7e485](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5a7e48553fb45e31d25f454264dd9d59fe2e8ccc))
* delete blank lines at the end ([c25c08b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c25c08b9e912a685019556b9f799aef12e973b98))
* enclosing SQL queries in variables for clearer visualization + importing OS module to toggle test mode ([fc0a6ba](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fc0a6ba0a99f93dd8ac17c10f92d4616dccbe588))
* improve CLI output formatting with printc ([5618e27](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5618e27c04f66152ca91bd06fba2a31db3229502))
* make variables for d.results more comprehensible ([7cda984](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7cda9842f5b2931c833c15b50d45dbeb2bfb9445))


### Refactoring

* add CONTROLLER package to define GUI's behavior (consequences of interactions through the simple VIEW) ([95f3b5d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/95f3b5d563078e7f98fd19cc2be46bed1ec6d794))
* add ID incremental int parameter to have a primary key for operations on DB ([93cec48](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/93cec48e67ee0e17409d2bdeaff6428b45843781))
* add MODEL package to define data to be inserted in the GUI (detached from pure graphic) ([953ecc2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/953ecc22fb23255718ac72b670737196369ef272))
* add parameter so that tests will continue automatically without initializing and configuring a real DB asking for user inputs ([ddd7a0a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ddd7a0a258490ef93e7c535057e1583906ba7715))
* add reconfig() wrapper to safely reset configuration (instead of separately running delete() first and config() after to speed the process up) ([8fdd48a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8fdd48a6fbb81c8f9c2541b21e23e360840da9f6))
* add VIEW package to define the GUI detaching it from real db connections, entries etc. ([6790d9d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/6790d9dc8aa71e3fb6072d4ab713c01ee30f9634))
* adding extra possible positional (args) and keyword arguments (kwargs) ([f52e8b4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f52e8b42ad3faf83053f11d8d6571d30eb44bbe9))
* allow master password to be passed as argument to skip input prompt during tests running ([1a1cca4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/1a1cca4e83c07802e49b70c23a8d75de9dabd1f4))
* binding view callback to controller ([ffc8b8d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ffc8b8d7fe61576ed1b300e75d76ba93498ccafb))
* checks if a vault or db schema already exists and stores the result in self.schema. If no schema found, shows error message and button to start setup and self.open_setup guides the user through initialization ([772867e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/772867efa70ee542729d854e61cfc0f25bfdcbe0))
* clean up main function logic for add/extract options ([5ca9c1f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5ca9c1ff212a4cbf728ae7d4dcbb56901c315986))
* create password entry box with masked characters (•), add "unlock" button that calls the login validation method, add a secondary button "configure" that opens setup options. With the lambda we bind the login not only to the button, but also to keyboard's key Enter ([74ad5d4](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/74ad5d45bb3d948134755927e05f9b48e708f902))
* define import of the view function at the beginning of the file ([4d0a2fb](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4d0a2fb7e8e22a20ed8018498fc6a30fe72adf90))
* **demo:** passing on dummy function to interact safely with mocked GUI waiting for logic from controller ([185fe9e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/185fe9e4738469a03fce858d6df24cab0d48d083))
* duplicate files deletion ([4ddd8a1](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4ddd8a1f2b17bcea5b8f67eff8228c12ee3974ba))
* easier and quicker code to verify the correctness of the whole configuration flow + matching password on second try ([36a0f2c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/36a0f2c477de68ca55a1b803d58b965868848252))
* enhance add_entry function based on real db and cursor connection ([9b2908d](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9b2908debad9fdee4f19d48e38c6b198347b68c3))
* enhance delete_entry function based on real db and cursor connection ([2d4747b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2d4747b39bad52911cc27f44834a5258b4caee32))
* enhance edit_entry function based on real db and cursor connection ([a65d512](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a65d512c39dba73c9a60c534a6685abd9dfec486))
* enhance export_to_file function based on all updated entries ([8498a35](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8498a35550d40544858f3a20aeacfe7d48876a68))
* enhance get_entries function based on db and cursor connection ([2d521b2](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2d521b225a4d12fbe8850f56f7bdd0aa599c0cc1))
* enhance import_from_file function based on all updated entries ([7755475](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/7755475b5f0f259b949dea0bbfd2e877706d13ac))
* **GUI:** add try/except for add.py to compute the Master Key and handling the case in which the user has not got any add.py managing cryptography on the fly ([a1e2f31](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/a1e2f3192da97783c29bb8e54dc33f4287e54a11))
* **GUI:** add try/except for AES256util.py for encryption handling the case of import error or missing file ([5ec7db5](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5ec7db503bba7069bc6dc45290cf5d0f974832fd))
* **GUI:** add try/except for generate.py handling the situation in which the generation needs to be made on the fly faking generate with a generatePassword function ([2f990f9](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/2f990f9228d1a7aed81f94e998a96554ebdd84f4))
* **GUI:** add try/except for pyperclip library which is sued for copy and paste functionality (to clipboard) and handles the case in which the library is not present preventing it from crashing, yet resulting in None object ([181c9be](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/181c9bed40c0b18ddf2b909a0c08f4f2e228dd5c))
* **GUI:** authentication methods. verify_master() checks if the master password entered by the user matches the hash in the database. ([c0411a3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c0411a3f56ad960a6e9f9c095683d751c5144868))
* **GUI:** CRUD operations. Add a new password entry but encrypts it first (the whole row with all info has to be completed) ([5c4fc2a](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/5c4fc2a4f3f1f2d353710f1c2f319711d3e027ad))
* **GUI:** CRUD operations. gets all entries to populate the view in the GUI ([c012f5b](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c012f5b6a1c76ad6d4431e66abe9c5d97b1bd9cc))
* **GUI:** CRUD operations. Modifies an existing entry (re-encrypts the password if it gets changed) ([4c69d5e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/4c69d5e917a9ed12c65e518bf0355b00e73b81cf))
* **GUI:** CRUD operations. Removes a password entry (the whole row) ([f468f74](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/f468f74fa0da7754d92496de32027fc6faf7b469))
* **GUI:** lets users back up data truggering the GUI's export button ([dafe9be](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/dafe9be38534f9825c7ef5e0497b2d606054d5d3))
* **GUI:** lets users restore vault data triggering the GUI's import button ([ecc0e20](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ecc0e20f5b7acc07069dd217c6eb9b456b5b6a3f))
* implement DEMO-MODE so that we don't have to proceed with real initial configuration (just try the GUI out) ([45bb883](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/45bb8834e9680f6e648a8b7c6a9998af756f9dca))
* implementing PromptPassword class ([27f8df7](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/27f8df7993e10d478168b3ff512afe1c8239c745))
* **imports:** add try/except for dbconfig import with error handling ([b14037e](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/b14037e02dc3323e9a0e415262f480bcdbe1262c))
* lambda default avoids error if no controller connected yet ([8019e63](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/8019e63dd006f66abb1be2e8e81626edac92f377))
* open and prepare DB via the model to perform operations + compute and store encryption key derived from master password ([ec37230](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/ec372308488cde362dea0d60f23c41e40be68a81))
* passing the PasswordManagerView class inside init ([eab92f0](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/eab92f0ca5a190f488e1327b32a7f8af40181104))
* quicker and easier code to check how a failure in the configuration gets handled ([9bc3fcb](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/9bc3fcb905f100b0ce2b9427e7f0abb0eb4635bf))
* quicker and easier testing code in the scenario in which the schema is still missing ([c2062b8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/c2062b8ebbbda0f1470a7754b983ec1679f3d114))
* remove GUIdemo.py from ui folder (moved into devtools/) ([14fa8be](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/14fa8be0e4920ca73075e8feb7557e21cec29da9))
* rewriting part of the testing code to be quicker and easier ([fd6b9e8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/fd6b9e814c7c1b23e278caaae0c6334fa8a3368c))
* safer import specifications from AES256util ([eaa7b9f](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/eaa7b9ffc0206d051bdc8ca7d68f16831454d774))
* simpler and quicker test to check if the DB is already configured and make a warning message pop up ([16f2f84](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/16f2f847b3a50c901fffedb58bacf128fc976aa9))
* simplifying login verification to use fixed 'username', 'mp', and 'ds' columns ([e0666c3](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/e0666c38fdba72f5acb5c50a41aeb870af55d0af))
* simplifying signup to use fixed "username", "mp" and "ds" columns in secrets table ([45d63e8](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/45d63e80e15d34fbf24ba78e99cd5113e4415324))
* wire config, delete, and reconfig functions into CLI ([3042d7c](https://github.com/unibo-dtm-se-2425-PROtect/artifact/commit/3042d7cc99196ddba4441b318c5b5c915c2a7604))

## [1.0.1](https://github.com/aequitas-aod/template-python-project/compare/1.0.0...1.0.1) (2024-02-02)


### Dependency updates

* **deps:** update dependency pandas to v2.1.2 ([8fe0d36](https://github.com/aequitas-aod/template-python-project/commit/8fe0d36a83c74ff23c059735a69f91ebef4904f3))
* **deps:** update dependency pandas to v2.1.3 ([27eb2b6](https://github.com/aequitas-aod/template-python-project/commit/27eb2b6e5cd7bdac497412095bdd71ee8bc9f12c))
* **deps:** update dependency pandas to v2.1.4 ([cd2b1d4](https://github.com/aequitas-aod/template-python-project/commit/cd2b1d4c3d22d352a89d57794402df9c8779b5c6))
* **deps:** update dependency pandas to v2.2.0 ([b8df6b1](https://github.com/aequitas-aod/template-python-project/commit/b8df6b14bdb94a9e4d290a67ae9090227da61d29))
* **deps:** update dependency scikit-learn to v1.3.2 ([fe7eea2](https://github.com/aequitas-aod/template-python-project/commit/fe7eea22d078a77ed77477a78785c387953888f8))
* **deps:** update dependency scikit-learn to v1.4.0 ([85de0ed](https://github.com/aequitas-aod/template-python-project/commit/85de0ed24d38277ea86a7ac71781631c097e8aaf))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.69 ([fa07343](https://github.com/aequitas-aod/template-python-project/commit/fa07343c199db9cf3a0784abdf1858983f80392c))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.70 ([2f7eb9b](https://github.com/aequitas-aod/template-python-project/commit/2f7eb9b20f5fc44a154c18cdf4ddb413da9819fc))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.71 ([e7efd4f](https://github.com/aequitas-aod/template-python-project/commit/e7efd4f39ac7396621ae9a7182c42975d8756476))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.72 ([17cd38c](https://github.com/aequitas-aod/template-python-project/commit/17cd38c5f6969e7be37be61087c63047d462e00a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.73 ([ceba297](https://github.com/aequitas-aod/template-python-project/commit/ceba297fb66930fa41cfcc36794f37b16d041c60))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.74 ([a7c030d](https://github.com/aequitas-aod/template-python-project/commit/a7c030de41394700cc0cec89358e59a3709377b2))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.75 ([21e6b9a](https://github.com/aequitas-aod/template-python-project/commit/21e6b9af441d069af6c13ccbd55bad63d4a9a841))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.76 ([fcf51ce](https://github.com/aequitas-aod/template-python-project/commit/fcf51ce4d1048739ca4933ef56cefe69b1f25bb9))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.77 ([24c1ad5](https://github.com/aequitas-aod/template-python-project/commit/24c1ad5c7c2a6df6f8519c4bd3bfd9892cac7bdd))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.78 ([4881854](https://github.com/aequitas-aod/template-python-project/commit/488185409ad1263b83838fba5b07136517c9fe52))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.79 ([b09d25f](https://github.com/aequitas-aod/template-python-project/commit/b09d25f30d81f9bc22cee76f3cf2fe72e1589e62))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.80 ([d9e55c5](https://github.com/aequitas-aod/template-python-project/commit/d9e55c51fa21cf880450cbeee619cca167e55cec))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.81 ([d2608f8](https://github.com/aequitas-aod/template-python-project/commit/d2608f87dc1bb2554c4db8bd8fe57fb75512efdb))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.82 ([22b0719](https://github.com/aequitas-aod/template-python-project/commit/22b0719f19296441890e9e6f122df45efd5e095e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.83 ([8f2ec20](https://github.com/aequitas-aod/template-python-project/commit/8f2ec20935428b99b28d412040689e56fa30a07e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.84 ([cb92e70](https://github.com/aequitas-aod/template-python-project/commit/cb92e703568dbf402c51434c510fd97cb6946c52))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.85 ([f05865d](https://github.com/aequitas-aod/template-python-project/commit/f05865d98e638d8c7192bfdb360898b7152400f9))
* **deps:** update node.js to 20.10 ([f393b2a](https://github.com/aequitas-aod/template-python-project/commit/f393b2a2fb2d3aa98b5c5a969ef4df442d5c79de))
* **deps:** update node.js to 20.11 ([63410da](https://github.com/aequitas-aod/template-python-project/commit/63410da68d5122d155caac39b6f99de19d619825))
* **deps:** update node.js to 20.9 ([d107ca2](https://github.com/aequitas-aod/template-python-project/commit/d107ca20dd8414ef39ab6b6b95740b3ae2c75f16))
* **deps:** update node.js to v20 ([61b7e25](https://github.com/aequitas-aod/template-python-project/commit/61b7e250a9afe02465f435c6b709b2fcc872e338))
* **deps:** update python docker tag to v3.12.0 ([b123d48](https://github.com/aequitas-aod/template-python-project/commit/b123d4847e25cc94e86faf1f5ec37a4e0b54e46d))
* **deps:** update python docker tag to v3.12.1 ([ac01a01](https://github.com/aequitas-aod/template-python-project/commit/ac01a014b54008d5c7af4916880413ba864f9a33))


### Bug Fixes

* **release:** include .python-version in MANIFEST.in ([9d794fa](https://github.com/aequitas-aod/template-python-project/commit/9d794faac19b032c5a0f149c3e5e44df018db17b))


### Build and continuous integration

* **deps:** update actions/setup-node action to v4 ([45c9acd](https://github.com/aequitas-aod/template-python-project/commit/45c9acdfed764240e4e150e65a4507205537a16a))
* **deps:** update actions/setup-python action to v5 ([66921e3](https://github.com/aequitas-aod/template-python-project/commit/66921e3580f3223689adf1665a323befbd9b3272))

## 1.0.0 (2023-10-12)


### Features

* add renaming script ([ed33dbc](https://github.com/aequitas-aod/template-python-project/commit/ed33dbc03a68a605e6df7a9465c6985ec9d1e130))
* first commit ([6ddc082](https://github.com/aequitas-aod/template-python-project/commit/6ddc08296facfe64fe912fcd00a255adb2806193))


### Dependency updates

* **deps:** node 18.18 ([73eec49](https://github.com/aequitas-aod/template-python-project/commit/73eec49c6fc53fe3158a0b94be99dcaf6eb328eb))
* **deps:** update dependencies ([0be2f8d](https://github.com/aequitas-aod/template-python-project/commit/0be2f8deb9b8218e509ea0926ceeb78a7a2baa70))
* **deps:** update python docker tag to v3.11.6 ([199ffe6](https://github.com/aequitas-aod/template-python-project/commit/199ffe6a498c6b26d358d97ac2ef7046da68e268))


### Bug Fixes

* readme ([f12fb0b](https://github.com/aequitas-aod/template-python-project/commit/f12fb0b17c08a18a7e145199234dc38d43fd0ddb))
* release workflow ([9c84ec1](https://github.com/aequitas-aod/template-python-project/commit/9c84ec1497a1f8c6c438a248107746df0fa7c612))
* renovate configuration ([0db8978](https://github.com/aequitas-aod/template-python-project/commit/0db89788ad8bef935fa97b77e7fa05aca749da28))


### Build and continuous integration

* enable semantic release ([648759b](https://github.com/aequitas-aod/template-python-project/commit/648759ba41fda0cad343493709a57bcb908f7229))
* fix release by installing correct version of node ([d809f17](https://github.com/aequitas-aod/template-python-project/commit/d809f17fc96c7295e0ec526161a56f558d49aa47))


### General maintenance

* **ci:** dry run release on testpypi for template project ([b90a25a](https://github.com/aequitas-aod/template-python-project/commit/b90a25a0f1f439e0bf548eec0bfae21b1f8c44b1))
* **ci:** use jq to parse package.json ([66af494](https://github.com/aequitas-aod/template-python-project/commit/66af494bc406d4b9b649153f910016cceb1b63ce))
* initial todo-list ([154e024](https://github.com/aequitas-aod/template-python-project/commit/154e024ac1bb8a1f1c99826ab2ed6a28e703a513))
* remove useless Dockerfile ([0272af7](https://github.com/aequitas-aod/template-python-project/commit/0272af71647e254f7622d38ace6000f0cbc7f17d))
* write some instructions ([7da9554](https://github.com/aequitas-aod/template-python-project/commit/7da9554a6e458c5fc253a222b295fbeb6a7862ec))
