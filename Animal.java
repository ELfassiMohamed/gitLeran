public class Animal {
	public final static void main (String[] args){
	String block = "Meow";
	var results = switch (block){
                        case "Lion" -> "Carnivore";
                        case "Rabbit" -> "vegetarian";
                        //default -> "Maybe a cat";
                        };
            System.out.println(results);
	}
}
