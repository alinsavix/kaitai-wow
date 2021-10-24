import os
import subprocess

from typing import Union

# from typing import List

# Other args to consider: --ignore-case,  --ignore-all-space
def filediff(reference: Union[str, os.PathLike], testfile: Union[str, os.PathLike],
             limit: int = 200) -> int:
    exe = "diff"
    args = [
        "--unified=0", "--minimal", "--speed-large-files", "--text",
        "--ignore-space-change", "--label", "REFERENCE", "--label", "OUTPUT",
        str(reference), str(testfile)
    ]
    # print(f"Executing command: {exe}", str.join(" ", args))
    # print(f"current dir is: {os.getcwd()}")
    # result = subprocess.run([exe] + args, stdin=None, check=True)
    with subprocess.Popen([exe] + args, universal_newlines=True, bufsize=1,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          stdin=subprocess.DEVNULL,
                          ) as proc:
        linecount = 0
        line = proc.stdout.readline()  # type: ignore
        while line and (limit == 0 or linecount < limit):
            linecount += 1
            print(line, end="")
            line = proc.stdout.readline()  # type: ignore

        # if we're here we either ran out of lines, or got too many lines
        # consume any extra lines
        #
        # FIXME: This is really, really slow, even if we just turn it into
        # "kill diff when there's too many lines"... that latter one baffles
        # me.
        extra = 0
        while line:
            extra += 1
            line = proc.stdout.readline()  # type: ignore


        if extra > 0:
            print(f"WARNING: too many line differences, {extra} lines hidden")

        # hopefully diff is done, reap it
        try:
            proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()

        return proc.returncode


# below from previous subprocess w/ output capture thing
    # success = True
    # failmsg = None
    # with open(outfile, "w") as stdout, open(errfile, "w") as stderr:
    #     try:
    #         os.environ['PYTHONUNBUFFERED'] = "1"
    #         result = subprocess.run([exe] + args, stdin=None, stdout=stdout,
    #                                 stderr=stderr, timeout=timeout, check=True)
    #     except (subprocess.CalledProcessError) as e:
    #         t = type(e).__name__
    #         success = False
    #         failmsg = f"{exe} process failed ({t}), exit code: {e.returncode}"
    #     except (OSError) as e:
    #         t = type(e).__name__
    #         success = False
    #         failmsg = f"error executing {exe}: {t} - {e}"
    # return success, failmsg
