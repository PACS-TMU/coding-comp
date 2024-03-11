public class TestCasesCountAndSay {
    private final CountAndSay ans = new CountAndSay();

    public void testAll() {
        int fail = 0;

        // Test case 1
        String result1 = ans.sayCount("312211");
        if (!result1.equals("13112221")) {
            System.out.println("Test case 1 failed. Expected: 13112221, Actual: " + result1);
            fail += 1;
        }

        // Test case 2
        String result2 = ans.sayCount("13112221");
        if (!result2.equals("1113213211")) {
            System.out.println("Test case 2 failed. Expected: 1113213211, Actual: " + result2);
            fail += 1;
        }

        // Test case 3
        String result3 = ans.sayCount("123456789");
        if (!result3.equals("111213141516171819")) {
            System.out.println("Test case 3 failed. Expected: 111213141516171819, Actual: " + result3);
            fail += 1;
        }

        // Test case 4
        String result4 = ans.sayCount("11133112");
        if (!result4.equals("31232112")) {
            System.out.println("Test case 4 failed. Expected: 11133112, Actual: " + result4);
            fail += 1;
        }

        // Test case 5
        String result5 = ans.sayCount("111112230");
        if (!result5.equals("51221310")) {
            System.out.println("Test case 5 failed. Expected: 51221310, Actual: " + result5);
            fail += 1;
        }

        // Test case 6
        String result6 = ans.sayCount("");
        if (!result6.equals("")) {
            System.out.println("Test case 6 failed. Expected: \"\", Actual: " + result6);
            fail += 1;
        }

        // Test case 7
        String result7 = ans.sayCount(null);
        if (result7 != "") {
            System.out.println("Test case 7 failed. Expected: null, Actual: " + result7);
            fail += 1;
        }

        String result8 = ans.sayCount("6");
        if (!result8.equals("16")) {
            System.out.println("Test case 8 failed. Expected: 16, Actual: " + result8);
            fail += 1;
        }

        System.out.println("-------------------------------------------------------------------");
        System.out.println("Ran 8 tests");
        if (fail > 0) {
            System.out.println();
            System.out.println("FAILED (failures="+fail+")");
        } else {
            System.out.println();
            System.out.println("OK");
        }
    }
}
