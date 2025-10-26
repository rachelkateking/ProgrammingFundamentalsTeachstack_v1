def test_basic_while(capsys):
    """
    Tests the while loop prints 1 to 5
    """
    from basic_while import main
    
    # Run the script
    main()
    output = capsys.readouterr().out.strip().split("\n")

    # Check that it prints numbers 1 through 5
    assert output == [str(i) for i in range(1, 6)], "The loop should print 1 through 5, each on a new line"
