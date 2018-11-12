from girder import plugin
from girder.api.rest import Resource


class Modsquad(Resource):
    def __init__(self):
        super(Modsquad, self).__init__()
        self.resourceName = 'modsquad'

        # Config
        self.route('GET', ('config',), self.getConfig)

        # Datasets.
        self.route('GET', ('dataset', 'data'), self.getDataset)
        self.route('GET', ('dataset', 'features'), self.getDatasetFeatures)
        self.route('GET', ('dataset', 'metadata'), self.getFeatureMetadata)
        self.route('GET', ('dataset', 'problems'), self.getProblems)

        # Pipelines.
        self.route('GET', ('pipeline', 'results'), self.getResults)
        self.route('POST', ('pipeline',), self.createPipeline)
        self.route('POST', ('pipeline', 'export'), self.executePipeline)
        self.route('POST', ('pipeline', 'results'), self.exportPipeline)

        # Stop process.
        self.route('POST', ('stop',), self.stopProcess)

        def getConfig():
            return {'foo': 'bar'}

        def getDataset():
            return {'foo': 'bar'}

        def getDatasetFeatures():
            return {'foo': 'bar'}

        def getFeatureMetadata():
            return {'foo': 'bar'}

        def getProblems():
            return {'foo': 'bar'}

        def getResults():
            return {'foo': 'bar'}

        def createPipeline():
            return {'foo': 'bar'}

        def executePipeline():
            return {'foo': 'bar'}

        def exportPipeline():
            return {'foo': 'bar'}

        def stopProcess():
            return {'foo': 'bar'}


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'Modsquad'

    def load(self, info):
        info['apiRoot'].modsquad = Modsquad()
