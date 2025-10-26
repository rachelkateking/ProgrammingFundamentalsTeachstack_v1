def test_break(capsys):
    """
    Tests the while loop counts from 1 to 5 and breaks
    """
    from loop_control import main
    
    # Run the script
    main()
    output = capsys.readouterr().out.strip().split("\n")

    # Check that it prints numbers 1 through 5 before breaking
    expected = [str(i) for i in range(1, 6)]
    assert output == expected, "The loop should print numbers 1 through 5 before breaking"