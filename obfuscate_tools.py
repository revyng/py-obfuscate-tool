import os

from pyminifier import obfuscate, token_utils, minification


class Options:
    def __init__(self, replacement_length):
        self.obfuscate = True
        self.replacement_length = replacement_length
        self.tabs = False


def identifier_obfuscate(src_file: str, dest_file: str, replacement_length: int):
    identifier_length = int(replacement_length)
    name_generator = obfuscate.obfuscation_machine(identifier_length=identifier_length)
    table = [{}]
    # Get the module name from the path
    module = os.path.split(src_file)[1]
    module = ".".join(module.split('.')[:-1])
    options = Options(replacement_length)
    source = open(src_file, encoding="utf8").read()
    tokens = token_utils.listified_tokenizer(source)
    source = minification.minify(tokens, options)
    # Convert back to tokens in case we're obfuscating
    tokens = token_utils.listified_tokenizer(source)
    # Perform obfuscation if any of the related options were set
    if name_generator:
        obfuscate.obfuscate(
            module,
            tokens,
            options,
            name_generator=name_generator,
            table=table
        )
    # Convert back to text
    result = ''
    result += token_utils.untokenize(tokens)
    # Compress it if we were asked to do so
    if not os.path.exists(dest_file):
        os.mkdir(dest_file)
    # Need the path where the script lives for the next steps:
    filepath = "obfuscate.py"
    path = dest_file + '/' + filepath  # Put everything in destdir
    f = open(path, 'w')
    f.write(result)
    f.close()
