def test_condition(capsys):
    """
    Tests the while loop sums numbers until exceeding 20
    """
    from while_condition import main
    
    # Run the script
    main()
    output = capsys.readouterr().out.strip()

    # Convert output to integer
    try:
        total = int(output)
    except ValueError:
        assert False, "The output should be a single number"

    # Check that the total is greater than 20 but was achieved by adding consecutive numbers from 1
    assert total > 20, "The total should be greater than 20"
    
    # Calculate what numbers were needed to exceed 20
    running_sum = 0
    last_num = 0
    for i in range(1, total + 1):
        running_sum += i
        if running_sum > 20:
            last_num = i
            break
    
    assert total == running_sum, "The total should be the sum of consecutive numbers from 1 until exceeding 20"