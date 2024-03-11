public class TestCasesPalindrome {
    private final ReversePalindrome ans = new ReversePalindrome();

    public void testAll() {
        int fail = 0;
        int pass = 0;

        // Test case 1
        Boolean result1 = ans.isPalindrome("racecar");
        if (result1 != true) {
            System.out.println("Test case 1 failed. Expected: true, Actual: " + result1);
            fail += 1;
        }
        else {
            System.out.println("Test case 1 passed. Expected: true, Actual: " + result1);
            pass += 1;
        }

        // Test case 2
        Boolean result2 = ans.isPalindrome("Level");
        if (result2 != true) {
            System.out.println("Test case 2 failed. Expected: true, Actual: " + result2);
            fail += 1;
        }
        else {
            System.out.println("Test case 2 passed. Expected: true, Actual: " + result2);
            pass += 1;
        }

        // Test case 3
        Boolean result3 = ans.isPalindrome("iateanapple");
        if (result3 != false) {
            System.out.println("Test case 3 failed. Expected: false, Actual: " + result3);
            fail += 1;
        }
        else {
            System.out.println("Test case 3 passed. Expected: false, Actual: " + result3);
            pass += 1;
        }

        // Test case 4
        Boolean result4 = ans.isPalindrome("");
        if (result4 != true) {
            System.out.println("Test case 4 failed. Expected: true, Actual: " + result4);
            fail += 1;
        }
        else {
            System.out.println("Test case 4 passed. Expected: true, Actual: " + result4);
            pass += 1;
        }

        // Test case 5
        Boolean result5 = ans.isPalindrome("10010");
        if (result5 != false) {
            System.out.println("Test case 5 failed. Expected: false, Actual: " + result5);
            fail += 1;
        }
        else {
            System.out.println("Test case 5 passed. Expected: false, Actual: " + result5);
            pass += 1;
        }

        // Test case 6
        Boolean result6 = ans.isPalindrome("12345654321");
        if (result6 != true) {
            System.out.println("Test case 6 failed. Expected: true, Actual: " + result6);
            fail += 1;
        }
        else {
            System.out.println("Test case 6 passed. Expected: true, Actual: " + result6);
            pass += 1;
        }

        // Test case 7
        Boolean result7 = ans.isPalindrome("MadamImAdam");
        if (result7 != true) {
            System.out.println("Test case 7 failed. Expected: true, Actual: " + result7);
            fail += 1;
        }
        else {
            System.out.println("Test case 7 passed. Expected: true, Actual: " + result7);
            pass += 1;
        }

        Boolean result8 = ans.isPalindrome("PACSTMU_UMTscap");
        if (result8 != true) {
            System.out.println("Test case 8 failed. Expected: true, Actual: " + result8);
            fail += 1;
        }
        else {
            System.out.println("Test case 8 passed. Expected: true, Actual: " + result8);
            pass += 1;
        }

        System.out.println("-------------------------------------------------------------------");
        System.out.println("Ran 8 tests");
        if (fail > 0) {
            System.out.println();
            System.out.println("FAILED (failures="+fail+")");
        } else {
            System.out.println();
            System.out.println("OK. Passed all " + pass + " test cases!");
        }
    }
}
