# lesson02_states: Difficulty Level: Intermediate

# Goal: Create a program that prints out an HTML drop down menu for all 50 states

# Step 1: Define your list of states
list_of_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District Of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
list_of_abbrs = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
print '<select>'
for i in range(len(list_of_states)):
    print '\t\t<option value="{1}">{0}</option>'.format(list_of_states[i], list_of_abbrs[i])
print '</select>'


outfile = open("states.html","w")
# insert the header row
outfile.write("<select>")
# output each of the rows
for i in range(len(list_of_states)):
    outfile.write ('\t\t<option value="{1}">{0}</option>'.format(list_of_states[i], list_of_abbrs[i]))
outfile.write("</select>")
# close output
outfile.close()
# Step 4: Test it!
# Have Python print out the HTML code. Copy / paste it into a file, save that file as "states.html" and open that file in a web browser.
# Later, when we learn file handling, we can skip the copy/paste step.
# File handling can also let us create a file with the state names and abbreviations in it so we don't have to add it to our code.

# Your finished project should look something like: https://github.com/shannonturner/python-lessons/blob/master/section_05_(loops)/states.html
