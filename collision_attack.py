'''
	2^16 variations of the legitimate message:

	{More efficient|Better} attacks are possible by {employing|using} cryptanalysis to specific hash functions. When a
	collision attack is {discovered|found} and is {found|determined} to be faster than a birthday attack, {a|the} hash function is often
	{denounced|termed} as "broken". The NIST hash function competition was largely induced by published collision
	attacks against {two|2} {very commonly | }used hash functions, MD5 and SHA-1. The {collision attacks|attacks} against
	MD5 have improved so much that, as of 2007, it {takes just|only takes} a {few|couple} seconds on a regular computer. {Hash
	collisions|Collisions} created this way are {usually|typically} constant length and largely unstructured, {so|so they} {cannot|can't} directly be
	{applied|used} to attack widespread document formats or protocols.

	
	2^16 variations of the fraudulent message:

	{As with|Similar to} encryption algorithms, cryptanalytic attacks on hash {functions|algorithms} {seek|look} to
 	exploit some {property|attribute} of the {algorithm|hash algorithm} to {perform|create} {some|an} attack other than an
 	{exhaustive|brute force} search. The way to {measure|find} the resistance of {a hash algorithm|hash algorithms} to cryptanalysis
	is to compare its strength to the effort required for a brute{-| }force attack.
	{That is|In other words}, {an ideal|a good} {hash algorithm|hash} will {require|need} a cryptanalytic effort greater than or
	equal to the brute{-| }force effort.
'''


# Hash size for this example will be 32 bits
HASH_SIZE = 32

# simple hash function
# May not be secure but it will serve its purpose in demonstrating a collision attack
def my_hash(message, m):
	size = 2**m
	return hash(message) % size

#take a message template and generate a list of all variations of the message
def createAlternates(messageTemplate):
	messages = [messageTemplate] * (2**(HASH_SIZE/2))

	# choose different alternates for each message
	for i in range(len(messages)):
		for j in range(HASH_SIZE/2):

			#find the jth alternate text
			altIndexStart = messages[i].find("{")
			altIndexMiddle = messages[i].find("|", altIndexStart)
			altIndexEnd = messages[i].find("}", altIndexMiddle)
			alt1 = messages[i][altIndexStart+1: altIndexMiddle]
			alt2 = messages[i][altIndexMiddle+1: altIndexEnd]

			# choose which alt to use for this message at this spot
			if (i >> j) & 1 == 0:
				messages[i] = messages[i][:altIndexStart] + alt1 + messages[i][altIndexEnd+1:]
			else:
				messages[i] = messages[i][:altIndexStart] + alt2 + messages[i][altIndexEnd+1:]


	return messages


##############################################################

# Start by computing all variations of the valid message
print "Generating legitimate messages..."

# create an array of all messages
# initialize each entry with a template for the legitimate message
# The string contains 'alternates' in the form "{alt1|alt2}"
legitTemplate = """{More efficient|Better} attacks are possible by {employing|using} cryptanalysis to specific hash functions. When a
collision attack is {discovered|found} and is {found|determined} to be faster than a birthday attack, {a|the} hash function is often
{denounced|termed} as "broken". The NIST hash function competition was largely induced by published collision
attacks against {two|2} {very commonly | }used hash functions, MD5 and SHA-1. The {collision attacks|attacks} against
MD5 have improved so much that, as of 2007, it {takes just|only takes} a {few|couple} seconds on a regular computer. 
{Hash collisions|Collisions} created this way are {usually|typically} constant length and largely unstructured, 
{so|so they} {cannot|can't} directly be {applied|used} to attack widespread document formats or protocols."""

legitMessages = createAlternates(legitTemplate)

# Hash all the messages
hashes = {}
print "Hashing legitimate messages..."
for m in legitMessages:
	h = my_hash(m, HASH_SIZE)
	hashes[h] = m




# Compute all variations of the fraudulent message
print("Generating fradulent messages...")

fraudTemplate = """{As with|Similar to} encryption algorithms, cryptanalytic attacks on hash {functions|algorithms} {seek|look} to
exploit some {property|attribute} of the {algorithm|hash algorithm} to {perform|create} {some|an} attack other than an
{exhaustive|brute force} search. The way to {measure|find} the resistance of {a hash algorithm|hash algorithms} to cryptanalysis
is to compare its strength to the effort required for a brute{-| }force attack.
{That is|In other words}, {an ideal|a good} {hash algorithm|hash} will {require|need} a cryptanalytic effort greater than or
equal to the brute{-| }force effort."""

fraudMessages = createAlternates(fraudTemplate)

# Hash fraudulent messages and look for a collision
print "Hashing fraudulent messages..."
for m in fraudMessages:
	h = my_hash(m, HASH_SIZE)
	try: 
		hashes[h]
		print "\nFound collision!\n"
		print "Legitimate message:"
		print hashes[h]
		print ""
		print "Fraudulent message:"
		print m
		print ""
		print "Hash value:", h
		break
	except:
		continue



