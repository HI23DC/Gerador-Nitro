import platform
from dhooks import Webhook

hook = Webhook("https://discord.com/api/webhooks/745084487431618610/TLADyY3SZfc1DNZReiZOp6YeAaiIURzONkrJ2ApfTr5xuzL1rTwIrc4vq1EcQUW1G75O")

my_system = platform.uname()

system = my_system.system
node_name =my_system.node
release = my_system.release
version = my_system.version
machine = my_system.machine
processor = my_system.processor

hook.send("teste")

print("Sistema: " + system)
print("Nome do nó: " + node_name)
print("Liberação: " + release)
print("Versão: " + version)
print("Máquina: " + machine)
print("Processador: " + processor)
