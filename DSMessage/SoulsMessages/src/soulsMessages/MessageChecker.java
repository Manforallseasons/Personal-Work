package soulsMessages;
import java.util.List;
import java.util.Set;
import java.util.regex.*;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.Random;
import java.util.ArrayList;


public class MessageChecker {

	public static boolean matchesBoolean(String input, List<String> templates) {
		for (String template : templates) {
			Pattern pattern = Pattern.compile(template, Pattern.CASE_INSENSITIVE);
			if (pattern.matcher(input).matches()) {
				return true;
			}
		}
		return false;
	}
	
	private static String buildRegexGroup(Set<String> words) {
		return "(?:" + words.stream().map(Pattern::quote).collect(Collectors.joining("|")) + ")";
	}
	
	public static <T> T getRandomElement(Set<T> set) {
        if (set == null || set.isEmpty()) {
            return null;
        }

        List<T> list = new ArrayList<>(set);
        Random random = new Random();
        int randomIndex = random.nextInt(list.size());
        return list.get(randomIndex);
	}
	
	public static <T> T getRandomElement(List<T> list) {
        if (list == null || list.isEmpty()) {
            return null; // Return null for empty or null list
        }
        Random rand = new Random();
        int randomIndex = rand.nextInt(list.size());
        return list.get(randomIndex);
    }
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		Set<String> valid = Set.of("Enemy", "Tough Enemy", "Hollow", "Soldier", "Knight", "Sniper", "Caster", "Giant", "Skeleton",
				"Ghost", "Bug", "Poison bug", "Lizard", "Drake", "Flier", "Golem", "Statue", "Monster", "Strange Creature", "Demon",
				"Darkwraith", "Dragon", "Boss", "Saint", "Wretch", "Charmer", "Miscreant", "Liar", "Fatty", "Beanpole", "Merchant",
				"Blacksmith", "Master", "Prisoner", "Bonfire", "Fog Wall", "Humanity", "Lever", "Switch", "Key", "Treasure", "Chest",
				"Weapon", "Shield", "Projectile", "Armor", "Item", "Ring", "Sorcery Scroll", "Pyromancy Scroll", "Miracle Scroll", 
				"Ember", "Trap", "Covenant", "Amazing Key", "Amazing treasure", "Amazing chest", "Amazing weapon", "Amazing shield",
				"Amazing Projectile", "Amazing Armor", "Amazing item", "Amazing ring", "Amazing sorcery scroll", "Amazing pyromancy scroll",
				"Amazing miracle scroll", "Amazing ember", "Amazing trap", "Close-ranged battle", "Ranged battle", "Eliminating one at a time",
				"Luring it out", "Beating to a pulp", "Lying in ambush", "Stealth", "Mimicry", "Pincer attack", "Hitting them in one swoop",
			    "Fleeing", "Charging", "Stabbing in the back", "Sweeping attack", "Shield breaking", "Head shots", "Sorcery", "Pyromancy",
			    "Miracles", "Jumping off", "Sliding down", "Dashing through", "Rolling",
			    "Backstepping", "Jumping", "Attacking", "Holding with both hands", "Kicking", "A plunging attack", "Blocking", "Parrying",
			    "Locking-on", "Path", "Hidden path", "Shortcut", "Detour", "Illusionary wall", "Dead end", "Swamp", "Lava",
			    "Forest", "Cave", "Labyrinth", "Safe zone", "Danger zone", "Sniper spot", "Bright spot", "Dark spot", "Open area",
			    "Tight spot", "Hidden place", "Exchange", "Gorgeous view", "Fall", "Front", "Back", "Left", "Right", "Up", "Down",
			    "Feet", "Head", "Neck", "Stomach", "Arm", "Leg", "Heel", "Rear", "Tail", "Wings", "Anywhere",
			    "Strike", "Thrust", "Slash", "Magic", "Fire", "Lightning", "Critical hits", "Bleeding", "Poison", "Strong poison", "Curses",
			    "Divine", "Occult", "Crystal", "Chance", "Hint", "Secret", "Happiness", "Sorrow", "Life", "Death", "Undead",
			    "Elation", "Grief", "Hope", "Despair", "Light", "Dark", "Bravery", "Resignation", "Comfort", "Tears");
		
		String regexValid = buildRegexGroup(valid);
		
	        List<String> templates = List.of(
			regexValid + " ahead",
			"Be wary of " + regexValid,
			"Try " + regexValid,
			"Need " + regexValid,
			"Imminent " + regexValid,
			"Imminent " + regexValid + "...",
			"Weakness: " + regexValid,
			"" + regexValid,
			regexValid + "\\?",
			"Good luck",
			"I did it!",
			"Here!",
			"I can't take this",
			"I can't take this...",
			"Praise the Sun!"
	    	);

		System.out.println(matchesBoolean("Enemy ahead", templates));

	}
	

}
