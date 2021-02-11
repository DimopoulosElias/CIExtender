python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_blacklisting.php?addr=* -v0 --flush-session --tamper=shell_tamper --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic.php?addr=* -v0 --flush-session --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_b64.php?addr=* -v0 --flush-session --tamper=base64encode --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_hex.php?addr=* -v0 --flush-session --tamper=hex_encode --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_quote.php?addr=* -v0 --flush-session --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_double_quote.php?addr=* -v0 --flush-session --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_blacklisting.php?addr=* -v0 --flush-session --tamper=shell_tamper --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_non_space.php?addr=* -v0 --flush-session --tamper=bash_no_space --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_hash.php?string=* -v0 --flush-session --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_basic_auth.php?addr=* -v0 --flush-session --auth-type "BASIC" --auth-cred="admin:admin" --hostname --batch
python3 CIExtender.py -u http://www.local.con/commix-testbed/scenarios/regular/GET/classic_digest_auth.php?addr=* -v0 --flush-session --auth-type "DIGEST" --auth-cred="admin:admin" --hostname --batch
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/eval.php?user=* -v0 --flush-session  --hostname --batch
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/eval_b64.php?user=* -v0 --flush-session --tamper=base64encode --hostname --batch
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/preg_match.php?addr=127.0.0.1* -v0 --flush-session --hostname --batch
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/str_replace.php?user=* -v0 --flush-session --tamper=php_send2header --hostname --batch
python3 CIExtender.py -u http://local.con/commix-testbed/scenarios/regular/GET/create_function.php?user=* -v0 --flush-session --hostname --batch
