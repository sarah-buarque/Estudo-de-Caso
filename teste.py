import requests

BASE_URL = "http://127.0.0.1:5000"

score = 0

def print_result(name, success):
    global score
    if success:
        print(f"[✔] {name}")
        score += 3
    else:
        print(f"[✘] {name}")

def test_create_service():
    r = requests.post(f"{BASE_URL}/service", json={
        "nome": "Instalação",
        "descricao": "Teste",
        "preco_base": 100
    })
    ok = r.status_code in [200, 201]
    print_result("Criar service", ok)

    try:
        return r.json()["data"]["id"] if ok else None
    except:
        return None


def test_list_services():
    r = requests.get(f"{BASE_URL}/service")
    print_result("Listar services", r.status_code == 200)


def test_validation_service():
    r = requests.post(f"{BASE_URL}/service", json={})
    print_result("Validação service", r.status_code == 400)

def test_create_order(service_id):
    r = requests.post(f"{BASE_URL}/orders", json={
        "descricao": "Teste ordem",
        "status": "aberta",
        "service_id": service_id
    })
    ok = r.status_code in [200, 201]
    print_result("Criar order válida", ok)


def test_invalid_service():
    r = requests.post(f"{BASE_URL}/orders", json={
        "descricao": "Erro",
        "status": "aberta",
        "service_id": 999
    })
    print_result("Service inválido em order", r.status_code == 404)


def test_list_orders():
    r = requests.get(f"{BASE_URL}/orders")
    print_result("Listar orders", r.status_code == 200)


def test_orders_by_service(service_id):
    r = requests.get(f"{BASE_URL}/service/{service_id}/orders")
    print_result("Orders por service", r.status_code == 200)

print("\n🚀 Testes - Service e Orders\n")

sid = test_create_service()
test_list_services()

if sid:
    test_create_order(sid)
    test_orders_by_service(sid)

test_invalid_service()
test_list_orders()
test_validation_service()

print(f"\n🎯 Pontuação: {score}/30\n")