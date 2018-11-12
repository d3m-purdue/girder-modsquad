from girder import plugin
from girder.api import access
from girder.api.describe import Description
from girder.api.describe import autoDescribeRoute
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

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def getConfig(self):
        return {'foo': 'bar'}

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def getDataset(self):
        return {'foo': 'bar'}

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def getDatasetFeatures(self):
        return {'foo': 'bar'}

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def getFeatureMetadata(self):
        return {'foo': 'bar'}

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def getProblems(self):
        return {'foo': 'bar'}

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def getResults(self):
        return {'foo': 'bar'}

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def createPipeline(self):
        return {'foo': 'bar'}

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def executePipeline(self):
        return {'foo': 'bar'}

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def exportPipeline(self):
        return {'foo': 'bar'}

    @access.public
    @autoDescribeRoute(
        Description('Foobar')
    )
    def stopProcess(self):
        return {'foo': 'bar'}


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'Modsquad'

    def load(self, info):
        info['apiRoot'].modsquad = Modsquad()
