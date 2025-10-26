from unittest.mock import patch

def test_user_input(capsys):
    """
    Tests the while loop continues until user types 'exit'
    """
    # Mock user inputs: "hello", "test", "exit"
    inputs = ["hello", "test", "exit"]
    
    with patch('builtins.input', side_effect=inputs):
        from user_input_while import main
        
        # Run the script
        main()
        output = capsys.readouterr().out.strip().split("\n")
        
        # Check that the program echoed back the inputs before exit
        assert len(output) >= 2, "The program should echo at least the first two inputs"
        assert "hello" in output, "The program should echo 'hello'"
        assert "test" in output, "The program should echo 'test'"
        # We don't expect to see 'exit' in output since the loop should end when it's entered