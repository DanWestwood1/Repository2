# AQA CS AS Notes

## 3.5 Fundamentals of data representation

### 3.5.1 Number systems + natural numbers

#### Natural Numbers
**Definition**: Numbers which are countable.
**Examples**: 0,1,2,3,4

#### Real Numbers
**Definition**: Numbers which are possible
**Examples**: 0, 1.1, 2.1, -78
 
#### Rational Numbers
**Definition**: Numbers which can be represented as a fraction
**Examples**: 1/7, 2/9, 7/11

#### Irrational Numbers
**Definition**: Numbers which cannot be represented as a fraction
**Examples**: √2, √3

#### Ordinal Numbers
**Definition**: Numbers which represent the position of an item in a list

#### Integer Numbers
**Definition**: Whole numbers
**Examples**: 1,2,3,4,5

### 3.5.2 Number bases

#### Base 2
The binary number system.
Each _placement value_ is represented as a power of 2, unlike in denary, where it is represented as 10
These numbers can be denoted as 1010<sub>2</sub>. 
See [this site](https://bournetocode.com/projects/AQA_AS_Theory/pages/3-5.html) for more infomation

#### Base 10
The denary system.
These numbers can be denoted as 16<sub>10</sub>.
![alt text](C:/home/bourne-grammar.lincs.sch.uk/98dw11/Documents/Year 12/Computer Science 2015 - 2016/Images/Denary.PNG "Denary Placement Values")

#### Base 16
The Hexadecimal system.
These numbers can be denoted as 22<sub>16</sub>.
Because denary does not have 16 symbols to use, hexadecimal uses A,B,C,D,E,F

The denary, binary and hexadecimal numbers up to 15 are featured below:
![alt text](C:/home/bourne-grammar.lincs.sch.uk/98dw11/Documents/Year 12/Computer Science 2015 - 2016/Images/DBH.PNG "Denary Placement Values")


### 3.5.3 Units of information
bit = single digit of data (0 or 1
nibble = 4 bits
byte = 8 bits

The rest of the units of data are below:
![alt text](C:/home/bourne-grammar.lincs.sch.uk/98dw11/Documents/Year 12/Computer Science 2015 - 2016/Images/Bits.PNG "Denary Placement Values")

### 3.5.4 Binary number system

#### unsigned binary
Unsigned binary is binary which does not have a digit at the front indicating if the number is positive. The aximum value is 255, and the number of possible numbers is 256

#### unsigned binary arithmetics
##### Addition
0+0 = 0
1+0 = 1
1+1 = 10 (carry the 1 over to the next space)
1+1+1 = 11(carry the 1 over)

##### Multiplication
0*0 = 0
1*1 = 0
0*1 = 0

#### signed binary with two's complement
The most significant bit (msb) is the sign digit here, with a value of 0 representing positive, and a value of 1 representing negative. THe remaining bits represent the magnitude, however when the number is negative, all the magnitude bits are flipped to whichever number they are not, and you add 1 to the number(due to the fact that there is no -0)
The range of values for two's complement is from -128 to +127 (256 values)

##### Addition in two's complement binary
This works the same way as ordinary binary addition, except when the resulting value has nine bits instead of eight, or when the msb (8th bit) changes from 0 to 1 or vice versa. This scenario is called an overflow.

##### Subtraction in two's complement binary. 
Because you cannot subtract binary, you need to flip the number you are taking away into negative, then add the numbers together. (remember to flip all the magnitude bits, then add 1)

#### fixed point form binary representation of numbers with fractional parts
##### Place values in binary:
2^3 	2^2 	2^1 	2^0 	2^-1 	2^-2
8 		4 		2 		1 		0.5 	0.25 etc
So we can represent a decimal such as 7.75 as:
0		1 		1 		1 		1 		1

Unfortunately we cannot represent decimals which are not a multiple of 2 (6.22, 8,12) because it would take an enormous amount of bits to encode. A standard 8 bit system can represent decimals such as 0.5, 0.25, 0.125 and 0.0625, while still being able to represent 15 as a number.

### 3.5.5 Information encoding system

#### ASCII

The American Standard Code for Information Interchange is a way of representing characters on a computer.
It can represent 128 unique different characters (numbers, symbols and letters)
Because the numbers in ASCII are considered as characters, if you try to add two ASCII numbers together, The two characters are just put next to each other.
Eg, 6+6 = 66

#### Unicode

Unicode was invented later than ASCII as a way of storing different alphabets other than the english alphabet on computers.
Unicode version UTF - 8 uses 8 bits, UTF - 16 uses 16 bits and UTF - 32 uses 32 bits

#### Error checking and correction
During transmission of signals, digital information can suffer from noise (thunderstorms, blocked line of sight etc) which results in data corruption and an unreliable resulting message on the other end. Therefore we use error prevention methods to recognise when this has happened.

##### Parity bit
This is the simplest form of checking, and involves using signed bits. During a handshake, the parity is decided as even or odd, which means that numbers coming through should always be even or odd. If the number which comes through is not even when it should be, it must not be right. If the parity is even, the msb is converted to 0 or 1, so that the resulting number is always even. The same goes for odd parity.

Unfortunately, if the number in question undergoes two changes during transmission which cause it to stay even (a 0 turns to a 1 and a 1 turns to a 0), the number is unreliable, but is recognised by the receiving computer as correct. This method of checking is not very reliable. 

##### Majority voting

### 3.5.6 Representing images, sound and other data

#### Bit patterns, images,  sound  and other  data
#### Analogue and digital
#### Analogue and digital conversion
#### Bitmapped graphics
#### Digital representation of sound
#### Musical Instrument Digital Interface (MIDI)
#### Data compression
#### Encryption
