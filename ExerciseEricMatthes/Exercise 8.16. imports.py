# Cara 1: import module_name
import pesan
pesan.display_message()

# Cara 2: from module_name import function_name
from pesan import display_message
display_message()

# Cara 3: from module_name import function_name as fn
from pesan import display_message as tampilkan
tampilkan()

# Cara 4: import module_name as mn
import pesan as ps
ps.display_message()

# Cara 5: from module_name import *
from pesan import *
display_message()