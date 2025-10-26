def test_continue(capsys):
    """
    Tests the while loop prints odd numbers from 1 to 10
    """
    from continue_keyword import main
    
    # Run the script
    main()
    output = capsys.readouterr().out.strip().split("\n")

    # Check that it prints only odd numbers from 1 to 10
    expected = [str(i) for i in range(1, 11) if i % 2 != 0]
    assert output == expected, "The loop should print only odd numbers from 1 to 10"