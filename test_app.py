from add_number import add, main


def test_add_positive():
    assert add(10, 25) == 35


def test_add_negative():
    assert add(-5, 5) == 0


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Result: 10 + 25 = 35" in captured.out
