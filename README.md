# openmv
Cole, Vivi, William
April Tag Testing
Saturday January 13, 2024

*”Pinky Swear” —interlock fingers to equalize potential static electricity— before handing over a camera*

April Tag Distance Detection:
Normal Lens (H7 Board): 8.5 ft
Telephoto (Narrow) Lens (H7 Board): 23 ft
Snapshot’s Lens (H7 Plus Board): 6 ft 2 inches
Telephoto Global Shutter Ultra Monochrome Lens H7 Plus Board: 40 ft

Ultra-Wide Lens Tests for Note Detection (LAB colorspace)
Note on (light blue) tile floor:
L min: 15
L max: 62
A min: 4
A max: 65
B min: -11
B max: 65

Most likely to use on robot: Global Shutter Ultra Monochrome Lens
Cole, William, and Mr. Sarget
Serial Port Research 
Monday, January 15, 2024


Client Server
Half duplex communications where 1 person talks at time but multiple camera connections
Cameras turn on and listen to Roborio client
Roborio send request on bus (ID, command, args, … new line)
Identify separate commands with a new line
Cameras read ID and act depending on own ID
Rio gets message back, same ID, command responding to (first 2 bytes  the same for call and response), answer, … new line
Protocol definitions for each command and what will look like
Think about what values want to get back

Ex. April tags:
(3, a, new line)
(3, a, apriltag_ID, {centerX, centerY, distance, etc} *  the amount of april tags, quality)
 
Whiteboard talk:

        RoboRio  -----------------------------------------------------------------------> OpenMV Camera

- Game Piece(Vivi) GP
- Other Robots(Vivi)* OR
- AprtlTags(Cole) AT
- Line Detection(Cole) LD

<Camera ID, Cmd(GP, OR, AT, LD), Args..., New Line>                            <Camera ID, Same ID Sent, Args ..., New Line>





    OpenMV Camera  -------------------------------------------------------------------------> RoboRio

AprilTags:

<Camera ID, AT, Args[TagID, Center X, Center Y, rotation, distance, quality]
 * Num of AprilTags, New Line>                                                           Parce the information sent


---------------------------------------------------------------------------------------------------------------------

/* *Dictionary = Key:Value
	     X Size : 4
	     Y Size : 1 Billion*/
//Int = Whole Number, 1,2,3,4,5,etc...
//Double = Int + decmial, 1.2, 2.6, 3.8, etc...



Public Camera {
	this.id (int);
	this.cam-stats (dict*);
	this.apriltags (dict);
	this.gamepiece (dict);
	this.linedectection (dict);

	public class SerialComms{
		this.route (int);
		this.send (dict);
		this.recieve (dict);
	}

}
	






