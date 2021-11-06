# This is file with answers for homework «2.4. Инструменты Git»

1. Найдите полный хеш и комментарий коммита, хеш которого начинается на aefea.

**Command:** git show aefea

**Result:** _commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545_  and  _Update CHANGELOG.md_



2. Какому тегу соответствует коммит 85024d3?

**Command:** git show 85024d3

**Result:** _v0.12.23_



3. Сколько родителей у коммита b8d720? Напишите их хеши.

**Command:** git show b8d720

**Result:** _Merge: 56cd7859e 9ea88f22f_



4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24.

**Command:** git log --pretty=oneline v0.12.23...v0.12.24

**Result:**  _33ff1c03bb960b332be3af2e333462dde88b279e (tag: v0.12.24) v0.12.24_
_b14b74c4939dcab573326f4e3ee2a62e23e12f89 [Website] vmc provider links_
_3f235065b9347a758efadc92295b540ee0a5e26e Update CHANGELOG.md_
_6ae64e247b332925b872447e9ce869657281c2bf registry: Fix panic when server
achable_
_5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the get
arted guide's old location_
_06275647e2b53d97d4f0a19a0fec11f6d69820b5 Update CHANGELOG.md_
_d5f9411f5108260320064349b757f55c09bc4b80 command: Fix bug when using terr
ogin on Windows_
_4b6d06cc5dcb78af637bbb19c198faff37a066ed Update CHANGELOG.md_
_dd01a35078f040ca984cdd349f18d0b67e486c35 Update CHANGELOG.md_
_225466bc3e5f35baa5d07197bbc079345b77525e Cleanup after v0.12.23 release_

**Command:**  git show v0.12.23

**Result:**  _commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23) v0.12.23_ 



5. Найдите коммит в котором была создана функция func providerSource, ее определение в коде выглядит так func providerSource(...) (вместо троеточего перечислены аргументы).

**Command:** git grep -rl "func providerSource("

**Result:** _provider_source.go_

**Command:** git log -L :providerSource:provider_source.go

**Result:** _commit 8c928e83589d90a031f811fae52a81be7153e82f_



6. Найдите все коммиты в которых была изменена функция globalPluginDirs.

**Command:** git log -SglobalPluginDirs --oneline

**Result:** _35a058fb3 main: configure credentials from the CLI config fi_
_c0b176109 prevent log output during init_
_8364383c3 Push plugin discovery down into command package_



7. Кто автор функции synchronizedWriters?

**Command:** git log -SsynchronizedWriters --oneline

**Result:** _bdfea50cc remove unused_
_fd4f7eb0b remove prefixed io_
_5ac311e2a main: synchronize writes to VT100-faker on Windows_

**Command:** git show 5ac311

**Result:** _Author: Martin Atkins <mart@degeneration.co.uk>_



