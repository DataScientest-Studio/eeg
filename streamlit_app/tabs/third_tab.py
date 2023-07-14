import streamlit as st

sidebar_name = "Preprocessing"

title = "Méthodes de Preprocessing utilisées"
text = """Le pretraitemement des données, ou preprocessing, est
indispensable à l'analyse des signaux EEG et NIRS. Il permet notament
de s'étalonner par rapport aux électrodes de référence, de réduire les
bruits parasites, de supprimer les mauvais canaux, ou encore d'éliminer les
artéfacts de mouvement.
Les méthodes de preprocessing utilisées durant ce projet sont basées sur
celles proposées par les auteurs du dataset, ainsi que sur celles trouvées
dans d’autres articles scientifiques traitant de problématiques similaires.
"""

header1 = "Filtres numériques"
subheader11 = "Filtre passe-bande (passe-bas + passe-haut)"
text11= """Pour les données EEG, un filtre passe-haut de 0.01 HZ et un filtre
passe-bas de 24.49 Hz ont été appliqués. Ce sont des filtres utilisés de
manière conventionnelle dans l’analyse de signal EEG et qui permet de
conserver les signaux physiologiques tout en retirant des bruits parasites
comme le 60Hz (courant du casque) par exemple."""
subheader12 = "Filtre Butterworth"
text12= """Pour les données fNIRS, nous avons utilisé un filtre passe-bande
particulier, un filtre Butterworth d'ordre 4. Le gain de ce filtre est le
plus constant possible dans la bande passante et tend vers 0 dB dans la bande
de coupure.
"""

header2 = "Independant Components Analysis sur signal EEG"
text2 = """L'analyse en composantes indépendantes ou ICA permet d’identifier
et supprimer les artefacts pouvant provenir de diverses sources, telles
que les mouvements oculaires, les battements du coeur, les bruits électriques,
etc... L'ICA permet de séparer ces sources artefactuelles des signaux
cérébraux d'intérêt, facilitant ainsi une meilleure interprétation et
analyse des données.
"""

header3 = "Concentration en HbO et HbR sur signaux fNIRS"
text3 = """Les deux signaux utilisés en fNIRS correspondant à deux longueurs
d’onde (760 nm et 850 nm) ont également subi une transformation mathématique
pour les transformer en signaux de concentration d’hémoglobine oxygénée (HbO)
et d’hémoglobine désoxygénée (HbR). Cette transformation a été réalisée
en appliquant la loi de Beer-Lambert.
"""


def run():

    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.title(title)
    st.write(text)

    st.header(header1)
    st.subheader(subheader11)
    st.write(text11)
    st.subheader(subheader12)
    st.write(text12)

    st.header(header2)
    st.write(text2)

    st.header(header3)
    st.write(text3)

#    st.selectbox("Les différentes méthode de preprocessing",
#                ("ICA", "hbr","Butter"))
