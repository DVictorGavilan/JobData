HEADER: dict = {
    "name": "h1",
    "class": {"class": "h4 h6-xs text-center my-4"}
}
DIVS: dict = {
    "name": "div",
    "class": {"class": "p-3 border rounded mb-3 bg-white"}
}

JOB_NAME: dict = {
    "name": "a",
    "class": {"class": "font-weight-bold text-cyan-700"}
}

JOB_COMPANY: dict = {
    "name": "a",
    "class": {"class": "text-primary"}
}

JOB_TECHNOLOGIES_STACK: dict = {
    "name": "span",
    "class": {"class": "badge bg-gray-500 mx-1"}
}

JOB_DESCRIPTION: dict = {
    "name": "span",
    "class": {"class": "hidden-md-down text-gray-800"}
}

JOB_OTHER_DATA: dict = {
    "name": "div",
    "class": {"class": "col-12 col-lg-3 text-gray-700 pt-2 text-right hidden-md-down"}
}

PUBLICATION_DATE_PATTERN: str = r"([0-9]{0,2}[/][0-9]{0,2}[/][0-9]{0,4})"
WORKPLACE_LOCATION_PATTERN: str = r"(remoto|presencial|Hibrido|hibrido|híbrido|Híbrido)"
HAS_BEEN_UPDATED_PATTERN: str = "Actualizada"
SALARY_BAND_PATTERN: str = r"[0-9]{0,3}[.][0-9]{0,3}[€]"
CITIES_PATTERN: str = r"(Bruselas|A Coruña|Álava|Albacete|Alicante|Almería|Asturias|Ávila|Badajoz|Baleares|Barcelona|Bizkaia|Burgos|Cáceres|Cádiz|Cantabria|Castellón|Ceuta|Ciudad Real|Córdoba|Cuenca|Gipuzkoa|Girona|Granada|Guadalajara|Huelva|Huesca|Jaén|La Rioja|Palmas de Gran Canaria|León|Lugo|Lleida|Madrid|Málaga|Melilla|Murcia|Navarra|Ourense|Palencia|Pontevedra|Salamanca|Sta. Cruz de Tenerife|Segovia|Sevilla|Soria|Tarragona|Teruel|Toledo|Valencia|Valladolid|Zamora|Zaragoza)"
