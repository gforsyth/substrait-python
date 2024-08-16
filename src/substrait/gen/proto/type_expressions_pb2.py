"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..proto import type_pb2 as proto_dot_type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cproto/type_expressions.proto\x12\x05proto\x1a\x10proto/type.proto"\xdb-\n\x14DerivationExpression\x12)\n\x04bool\x18\x01 \x01(\x0b2\x13.proto.Type.BooleanH\x00R\x04bool\x12 \n\x02i8\x18\x02 \x01(\x0b2\x0e.proto.Type.I8H\x00R\x02i8\x12#\n\x03i16\x18\x03 \x01(\x0b2\x0f.proto.Type.I16H\x00R\x03i16\x12#\n\x03i32\x18\x05 \x01(\x0b2\x0f.proto.Type.I32H\x00R\x03i32\x12#\n\x03i64\x18\x07 \x01(\x0b2\x0f.proto.Type.I64H\x00R\x03i64\x12&\n\x04fp32\x18\n \x01(\x0b2\x10.proto.Type.FP32H\x00R\x04fp32\x12&\n\x04fp64\x18\x0b \x01(\x0b2\x10.proto.Type.FP64H\x00R\x04fp64\x12,\n\x06string\x18\x0c \x01(\x0b2\x12.proto.Type.StringH\x00R\x06string\x12,\n\x06binary\x18\r \x01(\x0b2\x12.proto.Type.BinaryH\x00R\x06binary\x129\n\ttimestamp\x18\x0e \x01(\x0b2\x15.proto.Type.TimestampB\x02\x18\x01H\x00R\ttimestamp\x12&\n\x04date\x18\x10 \x01(\x0b2\x10.proto.Type.DateH\x00R\x04date\x12&\n\x04time\x18\x11 \x01(\x0b2\x10.proto.Type.TimeH\x00R\x04time\x12?\n\rinterval_year\x18\x13 \x01(\x0b2\x18.proto.Type.IntervalYearH\x00R\x0cintervalYear\x12@\n\x0ctimestamp_tz\x18\x1d \x01(\x0b2\x17.proto.Type.TimestampTZB\x02\x18\x01H\x00R\x0btimestampTz\x12&\n\x04uuid\x18  \x01(\x0b2\x10.proto.Type.UUIDH\x00R\x04uuid\x12V\n\x0cinterval_day\x18\x14 \x01(\x0b21.proto.DerivationExpression.ExpressionIntervalDayH\x00R\x0bintervalDay\x12e\n\x11interval_compound\x18* \x01(\x0b26.proto.DerivationExpression.ExpressionIntervalCompoundH\x00R\x10intervalCompound\x12P\n\nfixed_char\x18\x15 \x01(\x0b2/.proto.DerivationExpression.ExpressionFixedCharH\x00R\tfixedChar\x12I\n\x07varchar\x18\x16 \x01(\x0b2-.proto.DerivationExpression.ExpressionVarCharH\x00R\x07varchar\x12V\n\x0cfixed_binary\x18\x17 \x01(\x0b21.proto.DerivationExpression.ExpressionFixedBinaryH\x00R\x0bfixedBinary\x12I\n\x07decimal\x18\x18 \x01(\x0b2-.proto.DerivationExpression.ExpressionDecimalH\x00R\x07decimal\x12k\n\x13precision_timestamp\x18( \x01(\x0b28.proto.DerivationExpression.ExpressionPrecisionTimestampH\x00R\x12precisionTimestamp\x12r\n\x16precision_timestamp_tz\x18) \x01(\x0b2:.proto.DerivationExpression.ExpressionPrecisionTimestampTZH\x00R\x14precisionTimestampTz\x12F\n\x06struct\x18\x19 \x01(\x0b2,.proto.DerivationExpression.ExpressionStructH\x00R\x06struct\x12@\n\x04list\x18\x1b \x01(\x0b2*.proto.DerivationExpression.ExpressionListH\x00R\x04list\x12=\n\x03map\x18\x1c \x01(\x0b2).proto.DerivationExpression.ExpressionMapH\x00R\x03map\x12V\n\x0cuser_defined\x18\x1e \x01(\x0b21.proto.DerivationExpression.ExpressionUserDefinedH\x00R\x0buserDefined\x126\n\x14user_defined_pointer\x18\x1f \x01(\rB\x02\x18\x01H\x00R\x12userDefinedPointer\x120\n\x13type_parameter_name\x18! \x01(\tH\x00R\x11typeParameterName\x126\n\x16integer_parameter_name\x18" \x01(\tH\x00R\x14integerParameterName\x12)\n\x0finteger_literal\x18# \x01(\x05H\x00R\x0eintegerLiteral\x12@\n\x08unary_op\x18$ \x01(\x0b2#.proto.DerivationExpression.UnaryOpH\x00R\x07unaryOp\x12C\n\tbinary_op\x18% \x01(\x0b2$.proto.DerivationExpression.BinaryOpH\x00R\x08binaryOp\x12=\n\x07if_else\x18& \x01(\x0b2".proto.DerivationExpression.IfElseH\x00R\x06ifElse\x12R\n\x0ereturn_program\x18\' \x01(\x0b2).proto.DerivationExpression.ReturnProgramH\x00R\rreturnProgram\x1a\xb2\x01\n\x13ExpressionFixedChar\x123\n\x06length\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\x06length\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xb0\x01\n\x11ExpressionVarChar\x123\n\x06length\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\x06length\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xb4\x01\n\x15ExpressionFixedBinary\x123\n\x06length\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\x06length\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xe9\x01\n\x11ExpressionDecimal\x121\n\x05scale\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\x05scale\x129\n\tprecision\x18\x02 \x01(\x0b2\x1b.proto.DerivationExpressionR\tprecision\x12+\n\x11variation_pointer\x18\x03 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x04 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xc1\x01\n\x1cExpressionPrecisionTimestamp\x129\n\tprecision\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\tprecision\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xba\x01\n\x15ExpressionIntervalDay\x129\n\tprecision\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\tprecision\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xbf\x01\n\x1aExpressionIntervalCompound\x129\n\tprecision\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\tprecision\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xc3\x01\n\x1eExpressionPrecisionTimestampTZ\x129\n\tprecision\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\tprecision\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xad\x01\n\x10ExpressionStruct\x121\n\x05types\x18\x01 \x03(\x0b2\x1b.proto.DerivationExpressionR\x05types\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1as\n\x15ExpressionNamedStruct\x12\x14\n\x05names\x18\x01 \x03(\tR\x05names\x12D\n\x06struct\x18\x02 \x01(\x0b2,.proto.DerivationExpression.ExpressionStructR\x06struct\x1a\xa9\x01\n\x0eExpressionList\x12/\n\x04type\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\x04type\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xd9\x01\n\rExpressionMap\x12-\n\x03key\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\x03key\x121\n\x05value\x18\x02 \x01(\x0b2\x1b.proto.DerivationExpressionR\x05value\x12+\n\x11variation_pointer\x18\x03 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x04 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xa2\x01\n\x15ExpressionUserDefined\x12!\n\x0ctype_pointer\x18\x01 \x01(\rR\x0btypePointer\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x129\n\x0bnullability\x18\x03 \x01(\x0e2\x17.proto.Type.NullabilityR\x0bnullability\x1a\xc0\x01\n\x06IfElse\x12>\n\x0cif_condition\x18\x01 \x01(\x0b2\x1b.proto.DerivationExpressionR\x0bifCondition\x128\n\tif_return\x18\x02 \x01(\x0b2\x1b.proto.DerivationExpressionR\x08ifReturn\x12<\n\x0belse_return\x18\x03 \x01(\x0b2\x1b.proto.DerivationExpressionR\nelseReturn\x1a\xcf\x01\n\x07UnaryOp\x12H\n\x07op_type\x18\x01 \x01(\x0e2/.proto.DerivationExpression.UnaryOp.UnaryOpTypeR\x06opType\x12-\n\x03arg\x18\x02 \x01(\x0b2\x1b.proto.DerivationExpressionR\x03arg"K\n\x0bUnaryOpType\x12\x1d\n\x19UNARY_OP_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19UNARY_OP_TYPE_BOOLEAN_NOT\x10\x01\x1a\xa8\x04\n\x08BinaryOp\x12J\n\x07op_type\x18\x01 \x01(\x0e21.proto.DerivationExpression.BinaryOp.BinaryOpTypeR\x06opType\x12/\n\x04arg1\x18\x02 \x01(\x0b2\x1b.proto.DerivationExpressionR\x04arg1\x12/\n\x04arg2\x18\x03 \x01(\x0b2\x1b.proto.DerivationExpressionR\x04arg2"\xed\x02\n\x0cBinaryOpType\x12\x1e\n\x1aBINARY_OP_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13BINARY_OP_TYPE_PLUS\x10\x01\x12\x18\n\x14BINARY_OP_TYPE_MINUS\x10\x02\x12\x1b\n\x17BINARY_OP_TYPE_MULTIPLY\x10\x03\x12\x19\n\x15BINARY_OP_TYPE_DIVIDE\x10\x04\x12\x16\n\x12BINARY_OP_TYPE_MIN\x10\x05\x12\x16\n\x12BINARY_OP_TYPE_MAX\x10\x06\x12\x1f\n\x1bBINARY_OP_TYPE_GREATER_THAN\x10\x07\x12\x1c\n\x18BINARY_OP_TYPE_LESS_THAN\x10\x08\x12\x16\n\x12BINARY_OP_TYPE_AND\x10\t\x12\x15\n\x11BINARY_OP_TYPE_OR\x10\n\x12\x19\n\x15BINARY_OP_TYPE_EQUALS\x10\x0b\x12\x19\n\x15BINARY_OP_TYPE_COVERS\x10\x0c\x1a\x8e\x02\n\rReturnProgram\x12V\n\x0bassignments\x18\x01 \x03(\x0b24.proto.DerivationExpression.ReturnProgram.AssignmentR\x0bassignments\x12F\n\x10final_expression\x18\x02 \x01(\x0b2\x1b.proto.DerivationExpressionR\x0ffinalExpression\x1a]\n\nAssignment\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12;\n\nexpression\x18\x02 \x01(\x0b2\x1b.proto.DerivationExpressionR\nexpressionB\x06\n\x04kindB#\n\x0eio.proto.protoP\x01\xaa\x02\x0eProto.Protobufb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.type_expressions_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x0eio.proto.protoP\x01\xaa\x02\x0eProto.Protobuf'
    _DERIVATIONEXPRESSION.fields_by_name['timestamp']._options = None
    _DERIVATIONEXPRESSION.fields_by_name['timestamp']._serialized_options = b'\x18\x01'
    _DERIVATIONEXPRESSION.fields_by_name['timestamp_tz']._options = None
    _DERIVATIONEXPRESSION.fields_by_name['timestamp_tz']._serialized_options = b'\x18\x01'
    _DERIVATIONEXPRESSION.fields_by_name['user_defined_pointer']._options = None
    _DERIVATIONEXPRESSION.fields_by_name['user_defined_pointer']._serialized_options = b'\x18\x01'
    _DERIVATIONEXPRESSION._serialized_start = 58
    _DERIVATIONEXPRESSION._serialized_end = 5909
    _DERIVATIONEXPRESSION_EXPRESSIONFIXEDCHAR._serialized_start = 2265
    _DERIVATIONEXPRESSION_EXPRESSIONFIXEDCHAR._serialized_end = 2443
    _DERIVATIONEXPRESSION_EXPRESSIONVARCHAR._serialized_start = 2446
    _DERIVATIONEXPRESSION_EXPRESSIONVARCHAR._serialized_end = 2622
    _DERIVATIONEXPRESSION_EXPRESSIONFIXEDBINARY._serialized_start = 2625
    _DERIVATIONEXPRESSION_EXPRESSIONFIXEDBINARY._serialized_end = 2805
    _DERIVATIONEXPRESSION_EXPRESSIONDECIMAL._serialized_start = 2808
    _DERIVATIONEXPRESSION_EXPRESSIONDECIMAL._serialized_end = 3041
    _DERIVATIONEXPRESSION_EXPRESSIONPRECISIONTIMESTAMP._serialized_start = 3044
    _DERIVATIONEXPRESSION_EXPRESSIONPRECISIONTIMESTAMP._serialized_end = 3237
    _DERIVATIONEXPRESSION_EXPRESSIONINTERVALDAY._serialized_start = 3240
    _DERIVATIONEXPRESSION_EXPRESSIONINTERVALDAY._serialized_end = 3426
    _DERIVATIONEXPRESSION_EXPRESSIONINTERVALCOMPOUND._serialized_start = 3429
    _DERIVATIONEXPRESSION_EXPRESSIONINTERVALCOMPOUND._serialized_end = 3620
    _DERIVATIONEXPRESSION_EXPRESSIONPRECISIONTIMESTAMPTZ._serialized_start = 3623
    _DERIVATIONEXPRESSION_EXPRESSIONPRECISIONTIMESTAMPTZ._serialized_end = 3818
    _DERIVATIONEXPRESSION_EXPRESSIONSTRUCT._serialized_start = 3821
    _DERIVATIONEXPRESSION_EXPRESSIONSTRUCT._serialized_end = 3994
    _DERIVATIONEXPRESSION_EXPRESSIONNAMEDSTRUCT._serialized_start = 3996
    _DERIVATIONEXPRESSION_EXPRESSIONNAMEDSTRUCT._serialized_end = 4111
    _DERIVATIONEXPRESSION_EXPRESSIONLIST._serialized_start = 4114
    _DERIVATIONEXPRESSION_EXPRESSIONLIST._serialized_end = 4283
    _DERIVATIONEXPRESSION_EXPRESSIONMAP._serialized_start = 4286
    _DERIVATIONEXPRESSION_EXPRESSIONMAP._serialized_end = 4503
    _DERIVATIONEXPRESSION_EXPRESSIONUSERDEFINED._serialized_start = 4506
    _DERIVATIONEXPRESSION_EXPRESSIONUSERDEFINED._serialized_end = 4668
    _DERIVATIONEXPRESSION_IFELSE._serialized_start = 4671
    _DERIVATIONEXPRESSION_IFELSE._serialized_end = 4863
    _DERIVATIONEXPRESSION_UNARYOP._serialized_start = 4866
    _DERIVATIONEXPRESSION_UNARYOP._serialized_end = 5073
    _DERIVATIONEXPRESSION_UNARYOP_UNARYOPTYPE._serialized_start = 4998
    _DERIVATIONEXPRESSION_UNARYOP_UNARYOPTYPE._serialized_end = 5073
    _DERIVATIONEXPRESSION_BINARYOP._serialized_start = 5076
    _DERIVATIONEXPRESSION_BINARYOP._serialized_end = 5628
    _DERIVATIONEXPRESSION_BINARYOP_BINARYOPTYPE._serialized_start = 5263
    _DERIVATIONEXPRESSION_BINARYOP_BINARYOPTYPE._serialized_end = 5628
    _DERIVATIONEXPRESSION_RETURNPROGRAM._serialized_start = 5631
    _DERIVATIONEXPRESSION_RETURNPROGRAM._serialized_end = 5901
    _DERIVATIONEXPRESSION_RETURNPROGRAM_ASSIGNMENT._serialized_start = 5808
    _DERIVATIONEXPRESSION_RETURNPROGRAM_ASSIGNMENT._serialized_end = 5901