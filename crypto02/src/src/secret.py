import os

MESSAGE = f"""Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
che la diritta via era smarrita.

Ahi quanto a dir qual era e' cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura!

Tant' e' amara che poco e' piu' morte;
ma per trattar del ben ch'i' vi trovai,
diro' de l'altre cose ch'i' v'ho scorte.
Ma una bella sorpresa m'apparve: {os.environ['FLAG']}""".lower().replace("\n", " ")