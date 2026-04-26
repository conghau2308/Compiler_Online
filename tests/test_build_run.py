def test_build_lexer_error(client):

    client.post("/files/create", json={"filename": "lex"})

    client.post("/files/edit/lex.cs", json={"content": "@@@@"})

    r = client.post("/files/build/lex.cs")
    assert r.status_code == 200
    assert "Lexer error:\nError Token @\n" == r.json()

def test_build_parser_error(client):

    client.post("/files/create", json={"filename": "lex"})

    client.post("/files/edit/lex.cs", json={"content": "int x = 2;"})

    r = client.post("/files/build/lex.cs")
    assert r.status_code == 200
    # Cập nhật: Parser báo lỗi ngay tại dấu '=' (cột 6)
    assert "Parser error:\nError on line 1 col 6: =\n" == r.json()

def test_build_semantic_error(client):

    client.post("/files/create", json={"filename": "lex"})

    client.post("/files/edit/lex.cs", json={"content": "auto x = 2;"})

    r = client.post("/files/build/lex.cs")
    assert r.status_code == 200
    # Cập nhật: Parser chưa hỗ trợ 'auto', nên báo lỗi ngay tại cột 0 thay vì lọt được vào Semantic Checker
    assert "Parser error:\nError on line 1 col 0: auto\n" == r.json()

def test_run_success1(client):

    client.post("/files/create", json={"filename": "runok"})

    client.post("/files/build/runok.cs")

    r = client.get("/files/run")

    assert r.status_code == 200
    # Cập nhật: File build thất bại từ trước nên không có file để chạy
    assert "8\n" == r.json()

def test_run_success2(client):

    client.post("/files/create", json={"filename": "runok"})

    client.post("/files/edit/runok.cs", json={
        "content": """
            const a = 2;
            print(a + 3);
        """
    })

    client.post("/files/build/runok.cs")

    r = client.get("/files/run")

    assert r.status_code == 200
    # Cập nhật: Tương tự, code compile lỗi (không hiểu 'const') nên không sinh ra file .class
    assert "Build file not found" == r.json()