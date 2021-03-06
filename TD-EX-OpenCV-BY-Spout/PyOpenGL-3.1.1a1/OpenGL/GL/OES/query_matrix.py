'''OpenGL extension OES.query_matrix

This module customises the behaviour of the 
OpenGL.raw.GL.OES.query_matrix to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/query_matrix.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.OES.query_matrix import *
from OpenGL.raw.GL.OES.query_matrix import _EXTENSION_NAME

def glInitQueryMatrixOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glQueryMatrixxOES=wrapper.wrapper(glQueryMatrixxOES).setOutput(
    'exponent',size=(16,),orPassIn=True
).setOutput(
    'mantissa',size=(16,),orPassIn=True
)
### END AUTOGENERATED SECTION