LABEL_STUDIO_URL = 'http://localhost:8080'
API_KEY = '02bde5a7e239bf8707ebd94559e278ff4a9f01fb'

# Import the SDK and the client module
from label_studio_sdk import Client

# Connect to the Label Studio API and check the connection
ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
ls.check_connection()

project = ls.start_project(
    title='Test Project',
    label_config='''
    <View>
        <Image name="image" value="$ocr"/>

        <Labels name="label" toName="image">
        <Label value="Text" background="green"/>
        <Label value="Handwriting" background="blue"/>
        </Labels>

        <Rectangle name="bbox" toName="image" strokeWidth="3"/>
        <Polygon name="poly" toName="image" strokeWidth="3"/>

        <TextArea name="transcription" toName="image"        
        editable="true"        
        perRegion="true"        
        required="true"        
        maxSubmissions="1"        
        rows="5"        
        placeholder="Recognized Text"        
        displayMode="region-list"    
        />
    </View>
    '''
)

project.import_tasks([{"image": ""}])
