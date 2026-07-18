public class ZooTest {
    public static void main(String[] args) {
        ZooTest test = new ZooTest();
        
        // Test with valid Number types
        test.openZoo(10);           // Integer
        test.openZoo(3.14);         // Double
        test.openZoo(100L);         // Long
        test.openZoo((short) 5);    // Short
        test.openZoo((byte) 2);     // Byte
        test.openZoo(10.5f);        // Float
        
        // Note: You cannot pass a String since the parameter is Number
        // This would cause a compilation error:
        // test.openZoo("10:00 AM"); // DOES NOT COMPILE
    }
    
    public void openZoo(Number time) {
        if(time instanceof Integer) { // DOES NOT COMPILE
            System.out.print("The time is :" +time);
        }
    }
}
