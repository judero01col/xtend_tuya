import json
import re

# JSON de dps
json_dps = '''
[
      {
        "code": "unlock_fingerprint",
        "custom_name": "",
        "dp_id": 1,
        "time": 1751294321000,
        "type": "value",
        "value": 10
      },
      {
        "code": "unlock_password",
        "custom_name": "",
        "dp_id": 2,
        "time": 1748717970604,
        "type": "value",
        "value": 0
      },
      {
        "code": "unlock_temporary",
        "custom_name": "",
        "dp_id": 3,
        "time": 1752069456000,
        "type": "value",
        "value": 904
      },
      {
        "code": "unlock_card",
        "custom_name": "",
        "dp_id": 5,
        "time": 1751293732000,
        "type": "value",
        "value": 14
      },
      {
        "code": "unlock_face",
        "custom_name": "",
        "dp_id": 6,
        "time": 1748717970604,
        "type": "value",
        "value": 0
      },
      {
        "code": "unlock_key",
        "custom_name": "",
        "dp_id": 7,
        "time": 1748717970604,
        "type": "value",
        "value": 0
      },
      {
        "code": "alarm_lock",
        "custom_name": "",
        "dp_id": 8,
        "time": 1748717970604,
        "type": "enum",
        "value": "wrong_finger"
      },
      {
        "code": "unlock_request",
        "custom_name": "",
        "dp_id": 9,
        "time": 1751830974701,
        "type": "value",
        "value": 0
      },
      {
        "code": "arming_switch",
        "custom_name": "",
        "dp_id": 10,
        "time": 1748717970604,
        "type": "bool",
        "value": false
      },
      {
        "code": "residual_electricity",
        "custom_name": "",
        "dp_id": 12,
        "time": 1752069466795,
        "type": "value",
        "value": 90
      },
      {
        "code": "unlock_app",
        "custom_name": "",
        "dp_id": 15,
        "time": 1748717970604,
        "type": "value",
        "value": 0
      },
      {
        "code": "open_inside",
        "custom_name": "",
        "dp_id": 17,
        "time": 1748717970604,
        "type": "bool",
        "value": false
      },
      {
        "code": "doorbell",
        "custom_name": "",
        "dp_id": 19,
        "time": 1751830937000,
        "type": "bool",
        "value": true
      },
      {
        "code": "unlock_hand",
        "custom_name": "",
        "dp_id": 23,
        "time": 1748717970604,
        "type": "value",
        "value": 0
      },
      {
        "code": "update_all_finger",
        "custom_name": "",
        "dp_id": 25,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "update_all_password",
        "custom_name": "",
        "dp_id": 26,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "update_all_card",
        "custom_name": "",
        "dp_id": 27,
        "time": 1751212140867,
        "type": "raw",
        "value": "AkA="
      },
      {
        "code": "update_all_face",
        "custom_name": "",
        "dp_id": 28,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "update_all_hand",
        "custom_name": "",
        "dp_id": 30,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "update_all_fin_vein",
        "custom_name": "",
        "dp_id": 31,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "unlock_offline_pd",
        "custom_name": "",
        "dp_id": 32,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "unlock_offline_clear",
        "custom_name": "",
        "dp_id": 33,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "remote_no_pd_setkey",
        "custom_name": "",
        "dp_id": 49,
        "time": 1748717977991,
        "type": "raw",
        "value": "AAAB"
      },
      {
        "code": "remote_no_dp_key",
        "custom_name": "",
        "dp_id": 50,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "lock_record",
        "custom_name": "",
        "dp_id": 57,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "local_capacity_link",
        "custom_name": "",
        "dp_id": 60,
        "time": 1748717970604,
        "type": "raw"
      },
      {
        "code": "lock_local_record",
        "custom_name": "",
        "dp_id": 70,
        "time": 1748717970604,
        "type": "raw"
      }
    ]
'''

# Contenido actual del enum (cadena de texto)
with open("const.py", encoding="utf-8") as f:
    existing_enum_text = f.read()

# Obtener todas las claves ya presentes en el enum
existing_codes = set(re.findall(r'^\s+([A-Z0-9_]+)\s*=\s*"([^"]+)"', existing_enum_text, re.MULTILINE))
existing_values = set(value for _, value in existing_codes)

# Cargar JSON
dp_list = json.loads(json_dps)

# Generar constantes faltantes
new_constants = []
for dp in dp_list:
    code = dp["code"]
    if code not in existing_values:
        const_name = re.sub(r'[^a-zA-Z0-9]', '_', code).upper()
        new_constants.append(f'    {const_name} = "{code}"')

# Mostrar el resultado
if new_constants:
    print("# Constantes faltantes:\n")
    print("\n".join(new_constants))
else:
    print("✅ No faltan constantes.")
