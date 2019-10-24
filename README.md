Dense Block

Keras Extended Dense Layer, Features Batch Normalization, Dropout and Dense layers, in that order, Created for convenient building of Complex Networks.

Args:
  units (int): Number of units on Dense Layer
  activation (str): Activation of Dense layer, default="relu"
  dropout (float): % of inputs to drop from Batch Normalization Layer
  l2 (float): Strenght of L2 regularization on Dense Layer

Call:
  inputs (float): Rank-2 Tensor of shape [Batch_Size, Input_Size]

Return:
  Rank-2 Tensor of shape [Batch_Size, units]
