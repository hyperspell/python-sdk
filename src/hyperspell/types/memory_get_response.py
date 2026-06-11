# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "MemoryGetResponse",
    "Document",
    "DocumentDocument",
    "DocumentDocumentChild",
    "DocumentDocumentChildBlob",
    "DocumentDocumentChildCallout",
    "DocumentDocumentChildCalloutChild",
    "DocumentDocumentChildCalloutChildBlob",
    "DocumentDocumentChildCalloutChildCode",
    "DocumentDocumentChildCalloutChildComment",
    "DocumentDocumentChildCalloutChildDivider",
    "DocumentDocumentChildCalloutChildImage",
    "DocumentDocumentChildCalloutChildLink",
    "DocumentDocumentChildCalloutChildLineBreak",
    "DocumentDocumentChildCalloutChildText",
    "DocumentDocumentChildCalloutChildToolCall",
    "DocumentDocumentChildCalloutChildToolResult",
    "DocumentDocumentChildCalloutChildTraceMessage",
    "DocumentDocumentChildChunk",
    "DocumentDocumentChildChunkChild",
    "DocumentDocumentChildChunkChildBlob",
    "DocumentDocumentChildChunkChildCode",
    "DocumentDocumentChildChunkChildComment",
    "DocumentDocumentChildChunkChildDivider",
    "DocumentDocumentChildChunkChildImage",
    "DocumentDocumentChildChunkChildLink",
    "DocumentDocumentChildChunkChildLineBreak",
    "DocumentDocumentChildChunkChildText",
    "DocumentDocumentChildChunkChildToolCall",
    "DocumentDocumentChildChunkChildToolResult",
    "DocumentDocumentChildChunkChildTraceMessage",
    "DocumentDocumentChildCode",
    "DocumentDocumentChildComment",
    "DocumentDocumentChildDivider",
    "DocumentDocumentChildEquation",
    "DocumentDocumentChildEquationChild",
    "DocumentDocumentChildEquationChildBlob",
    "DocumentDocumentChildEquationChildCode",
    "DocumentDocumentChildEquationChildComment",
    "DocumentDocumentChildEquationChildDivider",
    "DocumentDocumentChildEquationChildImage",
    "DocumentDocumentChildEquationChildLink",
    "DocumentDocumentChildEquationChildLineBreak",
    "DocumentDocumentChildEquationChildText",
    "DocumentDocumentChildEquationChildToolCall",
    "DocumentDocumentChildEquationChildToolResult",
    "DocumentDocumentChildEquationChildTraceMessage",
    "DocumentDocumentChildFootnote",
    "DocumentDocumentChildFootnoteChild",
    "DocumentDocumentChildFootnoteChildBlob",
    "DocumentDocumentChildFootnoteChildCode",
    "DocumentDocumentChildFootnoteChildComment",
    "DocumentDocumentChildFootnoteChildDivider",
    "DocumentDocumentChildFootnoteChildImage",
    "DocumentDocumentChildFootnoteChildLink",
    "DocumentDocumentChildFootnoteChildLineBreak",
    "DocumentDocumentChildFootnoteChildText",
    "DocumentDocumentChildFootnoteChildToolCall",
    "DocumentDocumentChildFootnoteChildToolResult",
    "DocumentDocumentChildFootnoteChildTraceMessage",
    "DocumentDocumentChildHeading",
    "DocumentDocumentChildHeadingChild",
    "DocumentDocumentChildHeadingChildBlob",
    "DocumentDocumentChildHeadingChildCode",
    "DocumentDocumentChildHeadingChildComment",
    "DocumentDocumentChildHeadingChildDivider",
    "DocumentDocumentChildHeadingChildImage",
    "DocumentDocumentChildHeadingChildLink",
    "DocumentDocumentChildHeadingChildLineBreak",
    "DocumentDocumentChildHeadingChildText",
    "DocumentDocumentChildHeadingChildToolCall",
    "DocumentDocumentChildHeadingChildToolResult",
    "DocumentDocumentChildHeadingChildTraceMessage",
    "DocumentDocumentChildImage",
    "DocumentDocumentChildLink",
    "DocumentDocumentChildLineBreak",
    "DocumentDocumentChildList",
    "DocumentDocumentChildListItem",
    "DocumentDocumentChildListItemChild",
    "DocumentDocumentChildListItemChildBlob",
    "DocumentDocumentChildListItemChildCode",
    "DocumentDocumentChildListItemChildComment",
    "DocumentDocumentChildListItemChildDivider",
    "DocumentDocumentChildListItemChildImage",
    "DocumentDocumentChildListItemChildLink",
    "DocumentDocumentChildListItemChildLineBreak",
    "DocumentDocumentChildListItemChildText",
    "DocumentDocumentChildListItemChildToolCall",
    "DocumentDocumentChildListItemChildToolResult",
    "DocumentDocumentChildListItemChildTraceMessage",
    "DocumentDocumentChildParagraph",
    "DocumentDocumentChildParagraphChild",
    "DocumentDocumentChildParagraphChildBlob",
    "DocumentDocumentChildParagraphChildCode",
    "DocumentDocumentChildParagraphChildComment",
    "DocumentDocumentChildParagraphChildDivider",
    "DocumentDocumentChildParagraphChildImage",
    "DocumentDocumentChildParagraphChildLink",
    "DocumentDocumentChildParagraphChildLineBreak",
    "DocumentDocumentChildParagraphChildText",
    "DocumentDocumentChildParagraphChildToolCall",
    "DocumentDocumentChildParagraphChildToolResult",
    "DocumentDocumentChildParagraphChildTraceMessage",
    "DocumentDocumentChildQuote",
    "DocumentDocumentChildQuoteChild",
    "DocumentDocumentChildQuoteChildBlob",
    "DocumentDocumentChildQuoteChildCode",
    "DocumentDocumentChildQuoteChildComment",
    "DocumentDocumentChildQuoteChildDivider",
    "DocumentDocumentChildQuoteChildImage",
    "DocumentDocumentChildQuoteChildLink",
    "DocumentDocumentChildQuoteChildLineBreak",
    "DocumentDocumentChildQuoteChildText",
    "DocumentDocumentChildQuoteChildToolCall",
    "DocumentDocumentChildQuoteChildToolResult",
    "DocumentDocumentChildQuoteChildTraceMessage",
    "DocumentDocumentChildTable",
    "DocumentDocumentChildTableCell",
    "DocumentDocumentChildTableCellChild",
    "DocumentDocumentChildTableCellChildBlob",
    "DocumentDocumentChildTableCellChildCode",
    "DocumentDocumentChildTableCellChildComment",
    "DocumentDocumentChildTableCellChildDivider",
    "DocumentDocumentChildTableCellChildImage",
    "DocumentDocumentChildTableCellChildLink",
    "DocumentDocumentChildTableCellChildLineBreak",
    "DocumentDocumentChildTableCellChildText",
    "DocumentDocumentChildTableCellChildToolCall",
    "DocumentDocumentChildTableCellChildToolResult",
    "DocumentDocumentChildTableCellChildTraceMessage",
    "DocumentDocumentChildTableRow",
    "DocumentDocumentChildText",
    "DocumentDocumentChildToDo",
    "DocumentDocumentChildToDoChild",
    "DocumentDocumentChildToDoChildBlob",
    "DocumentDocumentChildToDoChildCode",
    "DocumentDocumentChildToDoChildComment",
    "DocumentDocumentChildToDoChildDivider",
    "DocumentDocumentChildToDoChildImage",
    "DocumentDocumentChildToDoChildLink",
    "DocumentDocumentChildToDoChildLineBreak",
    "DocumentDocumentChildToDoChildText",
    "DocumentDocumentChildToDoChildToolCall",
    "DocumentDocumentChildToDoChildToolResult",
    "DocumentDocumentChildToDoChildTraceMessage",
    "DocumentDocumentChildToolCall",
    "DocumentDocumentChildToolResult",
    "DocumentDocumentChildTraceMessage",
    "DocumentDocumentChildUtterance",
    "DocumentWebsite",
    "DocumentWebsiteChild",
    "DocumentWebsiteChildBlob",
    "DocumentWebsiteChildCallout",
    "DocumentWebsiteChildCalloutChild",
    "DocumentWebsiteChildCalloutChildBlob",
    "DocumentWebsiteChildCalloutChildCode",
    "DocumentWebsiteChildCalloutChildComment",
    "DocumentWebsiteChildCalloutChildDivider",
    "DocumentWebsiteChildCalloutChildImage",
    "DocumentWebsiteChildCalloutChildLink",
    "DocumentWebsiteChildCalloutChildLineBreak",
    "DocumentWebsiteChildCalloutChildText",
    "DocumentWebsiteChildCalloutChildToolCall",
    "DocumentWebsiteChildCalloutChildToolResult",
    "DocumentWebsiteChildCalloutChildTraceMessage",
    "DocumentWebsiteChildChunk",
    "DocumentWebsiteChildChunkChild",
    "DocumentWebsiteChildChunkChildBlob",
    "DocumentWebsiteChildChunkChildCode",
    "DocumentWebsiteChildChunkChildComment",
    "DocumentWebsiteChildChunkChildDivider",
    "DocumentWebsiteChildChunkChildImage",
    "DocumentWebsiteChildChunkChildLink",
    "DocumentWebsiteChildChunkChildLineBreak",
    "DocumentWebsiteChildChunkChildText",
    "DocumentWebsiteChildChunkChildToolCall",
    "DocumentWebsiteChildChunkChildToolResult",
    "DocumentWebsiteChildChunkChildTraceMessage",
    "DocumentWebsiteChildCode",
    "DocumentWebsiteChildComment",
    "DocumentWebsiteChildDivider",
    "DocumentWebsiteChildEquation",
    "DocumentWebsiteChildEquationChild",
    "DocumentWebsiteChildEquationChildBlob",
    "DocumentWebsiteChildEquationChildCode",
    "DocumentWebsiteChildEquationChildComment",
    "DocumentWebsiteChildEquationChildDivider",
    "DocumentWebsiteChildEquationChildImage",
    "DocumentWebsiteChildEquationChildLink",
    "DocumentWebsiteChildEquationChildLineBreak",
    "DocumentWebsiteChildEquationChildText",
    "DocumentWebsiteChildEquationChildToolCall",
    "DocumentWebsiteChildEquationChildToolResult",
    "DocumentWebsiteChildEquationChildTraceMessage",
    "DocumentWebsiteChildFootnote",
    "DocumentWebsiteChildFootnoteChild",
    "DocumentWebsiteChildFootnoteChildBlob",
    "DocumentWebsiteChildFootnoteChildCode",
    "DocumentWebsiteChildFootnoteChildComment",
    "DocumentWebsiteChildFootnoteChildDivider",
    "DocumentWebsiteChildFootnoteChildImage",
    "DocumentWebsiteChildFootnoteChildLink",
    "DocumentWebsiteChildFootnoteChildLineBreak",
    "DocumentWebsiteChildFootnoteChildText",
    "DocumentWebsiteChildFootnoteChildToolCall",
    "DocumentWebsiteChildFootnoteChildToolResult",
    "DocumentWebsiteChildFootnoteChildTraceMessage",
    "DocumentWebsiteChildHeading",
    "DocumentWebsiteChildHeadingChild",
    "DocumentWebsiteChildHeadingChildBlob",
    "DocumentWebsiteChildHeadingChildCode",
    "DocumentWebsiteChildHeadingChildComment",
    "DocumentWebsiteChildHeadingChildDivider",
    "DocumentWebsiteChildHeadingChildImage",
    "DocumentWebsiteChildHeadingChildLink",
    "DocumentWebsiteChildHeadingChildLineBreak",
    "DocumentWebsiteChildHeadingChildText",
    "DocumentWebsiteChildHeadingChildToolCall",
    "DocumentWebsiteChildHeadingChildToolResult",
    "DocumentWebsiteChildHeadingChildTraceMessage",
    "DocumentWebsiteChildImage",
    "DocumentWebsiteChildLink",
    "DocumentWebsiteChildLineBreak",
    "DocumentWebsiteChildList",
    "DocumentWebsiteChildListItem",
    "DocumentWebsiteChildListItemChild",
    "DocumentWebsiteChildListItemChildBlob",
    "DocumentWebsiteChildListItemChildCode",
    "DocumentWebsiteChildListItemChildComment",
    "DocumentWebsiteChildListItemChildDivider",
    "DocumentWebsiteChildListItemChildImage",
    "DocumentWebsiteChildListItemChildLink",
    "DocumentWebsiteChildListItemChildLineBreak",
    "DocumentWebsiteChildListItemChildText",
    "DocumentWebsiteChildListItemChildToolCall",
    "DocumentWebsiteChildListItemChildToolResult",
    "DocumentWebsiteChildListItemChildTraceMessage",
    "DocumentWebsiteChildParagraph",
    "DocumentWebsiteChildParagraphChild",
    "DocumentWebsiteChildParagraphChildBlob",
    "DocumentWebsiteChildParagraphChildCode",
    "DocumentWebsiteChildParagraphChildComment",
    "DocumentWebsiteChildParagraphChildDivider",
    "DocumentWebsiteChildParagraphChildImage",
    "DocumentWebsiteChildParagraphChildLink",
    "DocumentWebsiteChildParagraphChildLineBreak",
    "DocumentWebsiteChildParagraphChildText",
    "DocumentWebsiteChildParagraphChildToolCall",
    "DocumentWebsiteChildParagraphChildToolResult",
    "DocumentWebsiteChildParagraphChildTraceMessage",
    "DocumentWebsiteChildQuote",
    "DocumentWebsiteChildQuoteChild",
    "DocumentWebsiteChildQuoteChildBlob",
    "DocumentWebsiteChildQuoteChildCode",
    "DocumentWebsiteChildQuoteChildComment",
    "DocumentWebsiteChildQuoteChildDivider",
    "DocumentWebsiteChildQuoteChildImage",
    "DocumentWebsiteChildQuoteChildLink",
    "DocumentWebsiteChildQuoteChildLineBreak",
    "DocumentWebsiteChildQuoteChildText",
    "DocumentWebsiteChildQuoteChildToolCall",
    "DocumentWebsiteChildQuoteChildToolResult",
    "DocumentWebsiteChildQuoteChildTraceMessage",
    "DocumentWebsiteChildTable",
    "DocumentWebsiteChildTableCell",
    "DocumentWebsiteChildTableCellChild",
    "DocumentWebsiteChildTableCellChildBlob",
    "DocumentWebsiteChildTableCellChildCode",
    "DocumentWebsiteChildTableCellChildComment",
    "DocumentWebsiteChildTableCellChildDivider",
    "DocumentWebsiteChildTableCellChildImage",
    "DocumentWebsiteChildTableCellChildLink",
    "DocumentWebsiteChildTableCellChildLineBreak",
    "DocumentWebsiteChildTableCellChildText",
    "DocumentWebsiteChildTableCellChildToolCall",
    "DocumentWebsiteChildTableCellChildToolResult",
    "DocumentWebsiteChildTableCellChildTraceMessage",
    "DocumentWebsiteChildTableRow",
    "DocumentWebsiteChildText",
    "DocumentWebsiteChildToDo",
    "DocumentWebsiteChildToDoChild",
    "DocumentWebsiteChildToDoChildBlob",
    "DocumentWebsiteChildToDoChildCode",
    "DocumentWebsiteChildToDoChildComment",
    "DocumentWebsiteChildToDoChildDivider",
    "DocumentWebsiteChildToDoChildImage",
    "DocumentWebsiteChildToDoChildLink",
    "DocumentWebsiteChildToDoChildLineBreak",
    "DocumentWebsiteChildToDoChildText",
    "DocumentWebsiteChildToDoChildToolCall",
    "DocumentWebsiteChildToDoChildToolResult",
    "DocumentWebsiteChildToDoChildTraceMessage",
    "DocumentWebsiteChildToolCall",
    "DocumentWebsiteChildToolResult",
    "DocumentWebsiteChildTraceMessage",
    "DocumentWebsiteChildUtterance",
    "DocumentTask",
    "DocumentTaskChild",
    "DocumentTaskChildBlob",
    "DocumentTaskChildCallout",
    "DocumentTaskChildCalloutChild",
    "DocumentTaskChildCalloutChildBlob",
    "DocumentTaskChildCalloutChildCode",
    "DocumentTaskChildCalloutChildComment",
    "DocumentTaskChildCalloutChildDivider",
    "DocumentTaskChildCalloutChildImage",
    "DocumentTaskChildCalloutChildLink",
    "DocumentTaskChildCalloutChildLineBreak",
    "DocumentTaskChildCalloutChildText",
    "DocumentTaskChildCalloutChildToolCall",
    "DocumentTaskChildCalloutChildToolResult",
    "DocumentTaskChildCalloutChildTraceMessage",
    "DocumentTaskChildChunk",
    "DocumentTaskChildChunkChild",
    "DocumentTaskChildChunkChildBlob",
    "DocumentTaskChildChunkChildCode",
    "DocumentTaskChildChunkChildComment",
    "DocumentTaskChildChunkChildDivider",
    "DocumentTaskChildChunkChildImage",
    "DocumentTaskChildChunkChildLink",
    "DocumentTaskChildChunkChildLineBreak",
    "DocumentTaskChildChunkChildText",
    "DocumentTaskChildChunkChildToolCall",
    "DocumentTaskChildChunkChildToolResult",
    "DocumentTaskChildChunkChildTraceMessage",
    "DocumentTaskChildCode",
    "DocumentTaskChildComment",
    "DocumentTaskChildDivider",
    "DocumentTaskChildEquation",
    "DocumentTaskChildEquationChild",
    "DocumentTaskChildEquationChildBlob",
    "DocumentTaskChildEquationChildCode",
    "DocumentTaskChildEquationChildComment",
    "DocumentTaskChildEquationChildDivider",
    "DocumentTaskChildEquationChildImage",
    "DocumentTaskChildEquationChildLink",
    "DocumentTaskChildEquationChildLineBreak",
    "DocumentTaskChildEquationChildText",
    "DocumentTaskChildEquationChildToolCall",
    "DocumentTaskChildEquationChildToolResult",
    "DocumentTaskChildEquationChildTraceMessage",
    "DocumentTaskChildFootnote",
    "DocumentTaskChildFootnoteChild",
    "DocumentTaskChildFootnoteChildBlob",
    "DocumentTaskChildFootnoteChildCode",
    "DocumentTaskChildFootnoteChildComment",
    "DocumentTaskChildFootnoteChildDivider",
    "DocumentTaskChildFootnoteChildImage",
    "DocumentTaskChildFootnoteChildLink",
    "DocumentTaskChildFootnoteChildLineBreak",
    "DocumentTaskChildFootnoteChildText",
    "DocumentTaskChildFootnoteChildToolCall",
    "DocumentTaskChildFootnoteChildToolResult",
    "DocumentTaskChildFootnoteChildTraceMessage",
    "DocumentTaskChildHeading",
    "DocumentTaskChildHeadingChild",
    "DocumentTaskChildHeadingChildBlob",
    "DocumentTaskChildHeadingChildCode",
    "DocumentTaskChildHeadingChildComment",
    "DocumentTaskChildHeadingChildDivider",
    "DocumentTaskChildHeadingChildImage",
    "DocumentTaskChildHeadingChildLink",
    "DocumentTaskChildHeadingChildLineBreak",
    "DocumentTaskChildHeadingChildText",
    "DocumentTaskChildHeadingChildToolCall",
    "DocumentTaskChildHeadingChildToolResult",
    "DocumentTaskChildHeadingChildTraceMessage",
    "DocumentTaskChildImage",
    "DocumentTaskChildLink",
    "DocumentTaskChildLineBreak",
    "DocumentTaskChildList",
    "DocumentTaskChildListItem",
    "DocumentTaskChildListItemChild",
    "DocumentTaskChildListItemChildBlob",
    "DocumentTaskChildListItemChildCode",
    "DocumentTaskChildListItemChildComment",
    "DocumentTaskChildListItemChildDivider",
    "DocumentTaskChildListItemChildImage",
    "DocumentTaskChildListItemChildLink",
    "DocumentTaskChildListItemChildLineBreak",
    "DocumentTaskChildListItemChildText",
    "DocumentTaskChildListItemChildToolCall",
    "DocumentTaskChildListItemChildToolResult",
    "DocumentTaskChildListItemChildTraceMessage",
    "DocumentTaskChildParagraph",
    "DocumentTaskChildParagraphChild",
    "DocumentTaskChildParagraphChildBlob",
    "DocumentTaskChildParagraphChildCode",
    "DocumentTaskChildParagraphChildComment",
    "DocumentTaskChildParagraphChildDivider",
    "DocumentTaskChildParagraphChildImage",
    "DocumentTaskChildParagraphChildLink",
    "DocumentTaskChildParagraphChildLineBreak",
    "DocumentTaskChildParagraphChildText",
    "DocumentTaskChildParagraphChildToolCall",
    "DocumentTaskChildParagraphChildToolResult",
    "DocumentTaskChildParagraphChildTraceMessage",
    "DocumentTaskChildQuote",
    "DocumentTaskChildQuoteChild",
    "DocumentTaskChildQuoteChildBlob",
    "DocumentTaskChildQuoteChildCode",
    "DocumentTaskChildQuoteChildComment",
    "DocumentTaskChildQuoteChildDivider",
    "DocumentTaskChildQuoteChildImage",
    "DocumentTaskChildQuoteChildLink",
    "DocumentTaskChildQuoteChildLineBreak",
    "DocumentTaskChildQuoteChildText",
    "DocumentTaskChildQuoteChildToolCall",
    "DocumentTaskChildQuoteChildToolResult",
    "DocumentTaskChildQuoteChildTraceMessage",
    "DocumentTaskChildTable",
    "DocumentTaskChildTableCell",
    "DocumentTaskChildTableCellChild",
    "DocumentTaskChildTableCellChildBlob",
    "DocumentTaskChildTableCellChildCode",
    "DocumentTaskChildTableCellChildComment",
    "DocumentTaskChildTableCellChildDivider",
    "DocumentTaskChildTableCellChildImage",
    "DocumentTaskChildTableCellChildLink",
    "DocumentTaskChildTableCellChildLineBreak",
    "DocumentTaskChildTableCellChildText",
    "DocumentTaskChildTableCellChildToolCall",
    "DocumentTaskChildTableCellChildToolResult",
    "DocumentTaskChildTableCellChildTraceMessage",
    "DocumentTaskChildTableRow",
    "DocumentTaskChildText",
    "DocumentTaskChildToDo",
    "DocumentTaskChildToDoChild",
    "DocumentTaskChildToDoChildBlob",
    "DocumentTaskChildToDoChildCode",
    "DocumentTaskChildToDoChildComment",
    "DocumentTaskChildToDoChildDivider",
    "DocumentTaskChildToDoChildImage",
    "DocumentTaskChildToDoChildLink",
    "DocumentTaskChildToDoChildLineBreak",
    "DocumentTaskChildToDoChildText",
    "DocumentTaskChildToDoChildToolCall",
    "DocumentTaskChildToDoChildToolResult",
    "DocumentTaskChildToDoChildTraceMessage",
    "DocumentTaskChildToolCall",
    "DocumentTaskChildToolResult",
    "DocumentTaskChildTraceMessage",
    "DocumentTaskChildUtterance",
    "DocumentTaskComment",
    "DocumentTaskCommentSender",
    "DocumentTaskCommentSenderChild",
    "DocumentTaskCommentSenderChildBlob",
    "DocumentTaskCommentSenderChildCode",
    "DocumentTaskCommentSenderChildComment",
    "DocumentTaskCommentSenderChildDivider",
    "DocumentTaskCommentSenderChildImage",
    "DocumentTaskCommentSenderChildLink",
    "DocumentTaskCommentSenderChildLineBreak",
    "DocumentTaskCommentSenderChildText",
    "DocumentTaskCommentSenderChildToolCall",
    "DocumentTaskCommentSenderChildToolResult",
    "DocumentTaskCommentSenderChildTraceMessage",
    "DocumentTaskCommentChild",
    "DocumentTaskCommentChildBlob",
    "DocumentTaskCommentChildCallout",
    "DocumentTaskCommentChildCalloutChild",
    "DocumentTaskCommentChildCalloutChildBlob",
    "DocumentTaskCommentChildCalloutChildCode",
    "DocumentTaskCommentChildCalloutChildComment",
    "DocumentTaskCommentChildCalloutChildDivider",
    "DocumentTaskCommentChildCalloutChildImage",
    "DocumentTaskCommentChildCalloutChildLink",
    "DocumentTaskCommentChildCalloutChildLineBreak",
    "DocumentTaskCommentChildCalloutChildText",
    "DocumentTaskCommentChildCalloutChildToolCall",
    "DocumentTaskCommentChildCalloutChildToolResult",
    "DocumentTaskCommentChildCalloutChildTraceMessage",
    "DocumentTaskCommentChildChunk",
    "DocumentTaskCommentChildChunkChild",
    "DocumentTaskCommentChildChunkChildBlob",
    "DocumentTaskCommentChildChunkChildCode",
    "DocumentTaskCommentChildChunkChildComment",
    "DocumentTaskCommentChildChunkChildDivider",
    "DocumentTaskCommentChildChunkChildImage",
    "DocumentTaskCommentChildChunkChildLink",
    "DocumentTaskCommentChildChunkChildLineBreak",
    "DocumentTaskCommentChildChunkChildText",
    "DocumentTaskCommentChildChunkChildToolCall",
    "DocumentTaskCommentChildChunkChildToolResult",
    "DocumentTaskCommentChildChunkChildTraceMessage",
    "DocumentTaskCommentChildCode",
    "DocumentTaskCommentChildComment",
    "DocumentTaskCommentChildDivider",
    "DocumentTaskCommentChildEquation",
    "DocumentTaskCommentChildEquationChild",
    "DocumentTaskCommentChildEquationChildBlob",
    "DocumentTaskCommentChildEquationChildCode",
    "DocumentTaskCommentChildEquationChildComment",
    "DocumentTaskCommentChildEquationChildDivider",
    "DocumentTaskCommentChildEquationChildImage",
    "DocumentTaskCommentChildEquationChildLink",
    "DocumentTaskCommentChildEquationChildLineBreak",
    "DocumentTaskCommentChildEquationChildText",
    "DocumentTaskCommentChildEquationChildToolCall",
    "DocumentTaskCommentChildEquationChildToolResult",
    "DocumentTaskCommentChildEquationChildTraceMessage",
    "DocumentTaskCommentChildFootnote",
    "DocumentTaskCommentChildFootnoteChild",
    "DocumentTaskCommentChildFootnoteChildBlob",
    "DocumentTaskCommentChildFootnoteChildCode",
    "DocumentTaskCommentChildFootnoteChildComment",
    "DocumentTaskCommentChildFootnoteChildDivider",
    "DocumentTaskCommentChildFootnoteChildImage",
    "DocumentTaskCommentChildFootnoteChildLink",
    "DocumentTaskCommentChildFootnoteChildLineBreak",
    "DocumentTaskCommentChildFootnoteChildText",
    "DocumentTaskCommentChildFootnoteChildToolCall",
    "DocumentTaskCommentChildFootnoteChildToolResult",
    "DocumentTaskCommentChildFootnoteChildTraceMessage",
    "DocumentTaskCommentChildHeading",
    "DocumentTaskCommentChildHeadingChild",
    "DocumentTaskCommentChildHeadingChildBlob",
    "DocumentTaskCommentChildHeadingChildCode",
    "DocumentTaskCommentChildHeadingChildComment",
    "DocumentTaskCommentChildHeadingChildDivider",
    "DocumentTaskCommentChildHeadingChildImage",
    "DocumentTaskCommentChildHeadingChildLink",
    "DocumentTaskCommentChildHeadingChildLineBreak",
    "DocumentTaskCommentChildHeadingChildText",
    "DocumentTaskCommentChildHeadingChildToolCall",
    "DocumentTaskCommentChildHeadingChildToolResult",
    "DocumentTaskCommentChildHeadingChildTraceMessage",
    "DocumentTaskCommentChildImage",
    "DocumentTaskCommentChildLink",
    "DocumentTaskCommentChildLineBreak",
    "DocumentTaskCommentChildList",
    "DocumentTaskCommentChildListItem",
    "DocumentTaskCommentChildListItemChild",
    "DocumentTaskCommentChildListItemChildBlob",
    "DocumentTaskCommentChildListItemChildCode",
    "DocumentTaskCommentChildListItemChildComment",
    "DocumentTaskCommentChildListItemChildDivider",
    "DocumentTaskCommentChildListItemChildImage",
    "DocumentTaskCommentChildListItemChildLink",
    "DocumentTaskCommentChildListItemChildLineBreak",
    "DocumentTaskCommentChildListItemChildText",
    "DocumentTaskCommentChildListItemChildToolCall",
    "DocumentTaskCommentChildListItemChildToolResult",
    "DocumentTaskCommentChildListItemChildTraceMessage",
    "DocumentTaskCommentChildParagraph",
    "DocumentTaskCommentChildParagraphChild",
    "DocumentTaskCommentChildParagraphChildBlob",
    "DocumentTaskCommentChildParagraphChildCode",
    "DocumentTaskCommentChildParagraphChildComment",
    "DocumentTaskCommentChildParagraphChildDivider",
    "DocumentTaskCommentChildParagraphChildImage",
    "DocumentTaskCommentChildParagraphChildLink",
    "DocumentTaskCommentChildParagraphChildLineBreak",
    "DocumentTaskCommentChildParagraphChildText",
    "DocumentTaskCommentChildParagraphChildToolCall",
    "DocumentTaskCommentChildParagraphChildToolResult",
    "DocumentTaskCommentChildParagraphChildTraceMessage",
    "DocumentTaskCommentChildQuote",
    "DocumentTaskCommentChildQuoteChild",
    "DocumentTaskCommentChildQuoteChildBlob",
    "DocumentTaskCommentChildQuoteChildCode",
    "DocumentTaskCommentChildQuoteChildComment",
    "DocumentTaskCommentChildQuoteChildDivider",
    "DocumentTaskCommentChildQuoteChildImage",
    "DocumentTaskCommentChildQuoteChildLink",
    "DocumentTaskCommentChildQuoteChildLineBreak",
    "DocumentTaskCommentChildQuoteChildText",
    "DocumentTaskCommentChildQuoteChildToolCall",
    "DocumentTaskCommentChildQuoteChildToolResult",
    "DocumentTaskCommentChildQuoteChildTraceMessage",
    "DocumentTaskCommentChildTable",
    "DocumentTaskCommentChildTableCell",
    "DocumentTaskCommentChildTableCellChild",
    "DocumentTaskCommentChildTableCellChildBlob",
    "DocumentTaskCommentChildTableCellChildCode",
    "DocumentTaskCommentChildTableCellChildComment",
    "DocumentTaskCommentChildTableCellChildDivider",
    "DocumentTaskCommentChildTableCellChildImage",
    "DocumentTaskCommentChildTableCellChildLink",
    "DocumentTaskCommentChildTableCellChildLineBreak",
    "DocumentTaskCommentChildTableCellChildText",
    "DocumentTaskCommentChildTableCellChildToolCall",
    "DocumentTaskCommentChildTableCellChildToolResult",
    "DocumentTaskCommentChildTableCellChildTraceMessage",
    "DocumentTaskCommentChildTableRow",
    "DocumentTaskCommentChildText",
    "DocumentTaskCommentChildToDo",
    "DocumentTaskCommentChildToDoChild",
    "DocumentTaskCommentChildToDoChildBlob",
    "DocumentTaskCommentChildToDoChildCode",
    "DocumentTaskCommentChildToDoChildComment",
    "DocumentTaskCommentChildToDoChildDivider",
    "DocumentTaskCommentChildToDoChildImage",
    "DocumentTaskCommentChildToDoChildLink",
    "DocumentTaskCommentChildToDoChildLineBreak",
    "DocumentTaskCommentChildToDoChildText",
    "DocumentTaskCommentChildToDoChildToolCall",
    "DocumentTaskCommentChildToDoChildToolResult",
    "DocumentTaskCommentChildToDoChildTraceMessage",
    "DocumentTaskCommentChildToolCall",
    "DocumentTaskCommentChildToolResult",
    "DocumentTaskCommentChildTraceMessage",
    "DocumentTaskCommentChildUtterance",
    "DocumentTaskCommentMentionedUser",
    "DocumentTaskCommentMentionedUserChild",
    "DocumentTaskCommentMentionedUserChildBlob",
    "DocumentTaskCommentMentionedUserChildCode",
    "DocumentTaskCommentMentionedUserChildComment",
    "DocumentTaskCommentMentionedUserChildDivider",
    "DocumentTaskCommentMentionedUserChildImage",
    "DocumentTaskCommentMentionedUserChildLink",
    "DocumentTaskCommentMentionedUserChildLineBreak",
    "DocumentTaskCommentMentionedUserChildText",
    "DocumentTaskCommentMentionedUserChildToolCall",
    "DocumentTaskCommentMentionedUserChildToolResult",
    "DocumentTaskCommentMentionedUserChildTraceMessage",
    "DocumentPerson",
    "DocumentPersonChild",
    "DocumentPersonChildBlob",
    "DocumentPersonChildCode",
    "DocumentPersonChildComment",
    "DocumentPersonChildDivider",
    "DocumentPersonChildImage",
    "DocumentPersonChildLink",
    "DocumentPersonChildLineBreak",
    "DocumentPersonChildText",
    "DocumentPersonChildToolCall",
    "DocumentPersonChildToolResult",
    "DocumentPersonChildTraceMessage",
    "DocumentMessage",
    "DocumentMessageSender",
    "DocumentMessageSenderChild",
    "DocumentMessageSenderChildBlob",
    "DocumentMessageSenderChildCode",
    "DocumentMessageSenderChildComment",
    "DocumentMessageSenderChildDivider",
    "DocumentMessageSenderChildImage",
    "DocumentMessageSenderChildLink",
    "DocumentMessageSenderChildLineBreak",
    "DocumentMessageSenderChildText",
    "DocumentMessageSenderChildToolCall",
    "DocumentMessageSenderChildToolResult",
    "DocumentMessageSenderChildTraceMessage",
    "DocumentMessageChild",
    "DocumentMessageChildBlob",
    "DocumentMessageChildCallout",
    "DocumentMessageChildCalloutChild",
    "DocumentMessageChildCalloutChildBlob",
    "DocumentMessageChildCalloutChildCode",
    "DocumentMessageChildCalloutChildComment",
    "DocumentMessageChildCalloutChildDivider",
    "DocumentMessageChildCalloutChildImage",
    "DocumentMessageChildCalloutChildLink",
    "DocumentMessageChildCalloutChildLineBreak",
    "DocumentMessageChildCalloutChildText",
    "DocumentMessageChildCalloutChildToolCall",
    "DocumentMessageChildCalloutChildToolResult",
    "DocumentMessageChildCalloutChildTraceMessage",
    "DocumentMessageChildChunk",
    "DocumentMessageChildChunkChild",
    "DocumentMessageChildChunkChildBlob",
    "DocumentMessageChildChunkChildCode",
    "DocumentMessageChildChunkChildComment",
    "DocumentMessageChildChunkChildDivider",
    "DocumentMessageChildChunkChildImage",
    "DocumentMessageChildChunkChildLink",
    "DocumentMessageChildChunkChildLineBreak",
    "DocumentMessageChildChunkChildText",
    "DocumentMessageChildChunkChildToolCall",
    "DocumentMessageChildChunkChildToolResult",
    "DocumentMessageChildChunkChildTraceMessage",
    "DocumentMessageChildCode",
    "DocumentMessageChildComment",
    "DocumentMessageChildDivider",
    "DocumentMessageChildEquation",
    "DocumentMessageChildEquationChild",
    "DocumentMessageChildEquationChildBlob",
    "DocumentMessageChildEquationChildCode",
    "DocumentMessageChildEquationChildComment",
    "DocumentMessageChildEquationChildDivider",
    "DocumentMessageChildEquationChildImage",
    "DocumentMessageChildEquationChildLink",
    "DocumentMessageChildEquationChildLineBreak",
    "DocumentMessageChildEquationChildText",
    "DocumentMessageChildEquationChildToolCall",
    "DocumentMessageChildEquationChildToolResult",
    "DocumentMessageChildEquationChildTraceMessage",
    "DocumentMessageChildFootnote",
    "DocumentMessageChildFootnoteChild",
    "DocumentMessageChildFootnoteChildBlob",
    "DocumentMessageChildFootnoteChildCode",
    "DocumentMessageChildFootnoteChildComment",
    "DocumentMessageChildFootnoteChildDivider",
    "DocumentMessageChildFootnoteChildImage",
    "DocumentMessageChildFootnoteChildLink",
    "DocumentMessageChildFootnoteChildLineBreak",
    "DocumentMessageChildFootnoteChildText",
    "DocumentMessageChildFootnoteChildToolCall",
    "DocumentMessageChildFootnoteChildToolResult",
    "DocumentMessageChildFootnoteChildTraceMessage",
    "DocumentMessageChildHeading",
    "DocumentMessageChildHeadingChild",
    "DocumentMessageChildHeadingChildBlob",
    "DocumentMessageChildHeadingChildCode",
    "DocumentMessageChildHeadingChildComment",
    "DocumentMessageChildHeadingChildDivider",
    "DocumentMessageChildHeadingChildImage",
    "DocumentMessageChildHeadingChildLink",
    "DocumentMessageChildHeadingChildLineBreak",
    "DocumentMessageChildHeadingChildText",
    "DocumentMessageChildHeadingChildToolCall",
    "DocumentMessageChildHeadingChildToolResult",
    "DocumentMessageChildHeadingChildTraceMessage",
    "DocumentMessageChildImage",
    "DocumentMessageChildLink",
    "DocumentMessageChildLineBreak",
    "DocumentMessageChildList",
    "DocumentMessageChildListItem",
    "DocumentMessageChildListItemChild",
    "DocumentMessageChildListItemChildBlob",
    "DocumentMessageChildListItemChildCode",
    "DocumentMessageChildListItemChildComment",
    "DocumentMessageChildListItemChildDivider",
    "DocumentMessageChildListItemChildImage",
    "DocumentMessageChildListItemChildLink",
    "DocumentMessageChildListItemChildLineBreak",
    "DocumentMessageChildListItemChildText",
    "DocumentMessageChildListItemChildToolCall",
    "DocumentMessageChildListItemChildToolResult",
    "DocumentMessageChildListItemChildTraceMessage",
    "DocumentMessageChildParagraph",
    "DocumentMessageChildParagraphChild",
    "DocumentMessageChildParagraphChildBlob",
    "DocumentMessageChildParagraphChildCode",
    "DocumentMessageChildParagraphChildComment",
    "DocumentMessageChildParagraphChildDivider",
    "DocumentMessageChildParagraphChildImage",
    "DocumentMessageChildParagraphChildLink",
    "DocumentMessageChildParagraphChildLineBreak",
    "DocumentMessageChildParagraphChildText",
    "DocumentMessageChildParagraphChildToolCall",
    "DocumentMessageChildParagraphChildToolResult",
    "DocumentMessageChildParagraphChildTraceMessage",
    "DocumentMessageChildQuote",
    "DocumentMessageChildQuoteChild",
    "DocumentMessageChildQuoteChildBlob",
    "DocumentMessageChildQuoteChildCode",
    "DocumentMessageChildQuoteChildComment",
    "DocumentMessageChildQuoteChildDivider",
    "DocumentMessageChildQuoteChildImage",
    "DocumentMessageChildQuoteChildLink",
    "DocumentMessageChildQuoteChildLineBreak",
    "DocumentMessageChildQuoteChildText",
    "DocumentMessageChildQuoteChildToolCall",
    "DocumentMessageChildQuoteChildToolResult",
    "DocumentMessageChildQuoteChildTraceMessage",
    "DocumentMessageChildTable",
    "DocumentMessageChildTableCell",
    "DocumentMessageChildTableCellChild",
    "DocumentMessageChildTableCellChildBlob",
    "DocumentMessageChildTableCellChildCode",
    "DocumentMessageChildTableCellChildComment",
    "DocumentMessageChildTableCellChildDivider",
    "DocumentMessageChildTableCellChildImage",
    "DocumentMessageChildTableCellChildLink",
    "DocumentMessageChildTableCellChildLineBreak",
    "DocumentMessageChildTableCellChildText",
    "DocumentMessageChildTableCellChildToolCall",
    "DocumentMessageChildTableCellChildToolResult",
    "DocumentMessageChildTableCellChildTraceMessage",
    "DocumentMessageChildTableRow",
    "DocumentMessageChildText",
    "DocumentMessageChildToDo",
    "DocumentMessageChildToDoChild",
    "DocumentMessageChildToDoChildBlob",
    "DocumentMessageChildToDoChildCode",
    "DocumentMessageChildToDoChildComment",
    "DocumentMessageChildToDoChildDivider",
    "DocumentMessageChildToDoChildImage",
    "DocumentMessageChildToDoChildLink",
    "DocumentMessageChildToDoChildLineBreak",
    "DocumentMessageChildToDoChildText",
    "DocumentMessageChildToDoChildToolCall",
    "DocumentMessageChildToDoChildToolResult",
    "DocumentMessageChildToDoChildTraceMessage",
    "DocumentMessageChildToolCall",
    "DocumentMessageChildToolResult",
    "DocumentMessageChildTraceMessage",
    "DocumentMessageChildUtterance",
    "DocumentMessageMentionedUser",
    "DocumentMessageMentionedUserChild",
    "DocumentMessageMentionedUserChildBlob",
    "DocumentMessageMentionedUserChildCode",
    "DocumentMessageMentionedUserChildComment",
    "DocumentMessageMentionedUserChildDivider",
    "DocumentMessageMentionedUserChildImage",
    "DocumentMessageMentionedUserChildLink",
    "DocumentMessageMentionedUserChildLineBreak",
    "DocumentMessageMentionedUserChildText",
    "DocumentMessageMentionedUserChildToolCall",
    "DocumentMessageMentionedUserChildToolResult",
    "DocumentMessageMentionedUserChildTraceMessage",
    "DocumentEvent",
    "DocumentEventAttendee",
    "DocumentEventAttendeeChild",
    "DocumentEventAttendeeChildBlob",
    "DocumentEventAttendeeChildCode",
    "DocumentEventAttendeeChildComment",
    "DocumentEventAttendeeChildDivider",
    "DocumentEventAttendeeChildImage",
    "DocumentEventAttendeeChildLink",
    "DocumentEventAttendeeChildLineBreak",
    "DocumentEventAttendeeChildText",
    "DocumentEventAttendeeChildToolCall",
    "DocumentEventAttendeeChildToolResult",
    "DocumentEventAttendeeChildTraceMessage",
    "DocumentEventChild",
    "DocumentEventChildBlob",
    "DocumentEventChildCallout",
    "DocumentEventChildCalloutChild",
    "DocumentEventChildCalloutChildBlob",
    "DocumentEventChildCalloutChildCode",
    "DocumentEventChildCalloutChildComment",
    "DocumentEventChildCalloutChildDivider",
    "DocumentEventChildCalloutChildImage",
    "DocumentEventChildCalloutChildLink",
    "DocumentEventChildCalloutChildLineBreak",
    "DocumentEventChildCalloutChildText",
    "DocumentEventChildCalloutChildToolCall",
    "DocumentEventChildCalloutChildToolResult",
    "DocumentEventChildCalloutChildTraceMessage",
    "DocumentEventChildChunk",
    "DocumentEventChildChunkChild",
    "DocumentEventChildChunkChildBlob",
    "DocumentEventChildChunkChildCode",
    "DocumentEventChildChunkChildComment",
    "DocumentEventChildChunkChildDivider",
    "DocumentEventChildChunkChildImage",
    "DocumentEventChildChunkChildLink",
    "DocumentEventChildChunkChildLineBreak",
    "DocumentEventChildChunkChildText",
    "DocumentEventChildChunkChildToolCall",
    "DocumentEventChildChunkChildToolResult",
    "DocumentEventChildChunkChildTraceMessage",
    "DocumentEventChildCode",
    "DocumentEventChildComment",
    "DocumentEventChildDivider",
    "DocumentEventChildEquation",
    "DocumentEventChildEquationChild",
    "DocumentEventChildEquationChildBlob",
    "DocumentEventChildEquationChildCode",
    "DocumentEventChildEquationChildComment",
    "DocumentEventChildEquationChildDivider",
    "DocumentEventChildEquationChildImage",
    "DocumentEventChildEquationChildLink",
    "DocumentEventChildEquationChildLineBreak",
    "DocumentEventChildEquationChildText",
    "DocumentEventChildEquationChildToolCall",
    "DocumentEventChildEquationChildToolResult",
    "DocumentEventChildEquationChildTraceMessage",
    "DocumentEventChildFootnote",
    "DocumentEventChildFootnoteChild",
    "DocumentEventChildFootnoteChildBlob",
    "DocumentEventChildFootnoteChildCode",
    "DocumentEventChildFootnoteChildComment",
    "DocumentEventChildFootnoteChildDivider",
    "DocumentEventChildFootnoteChildImage",
    "DocumentEventChildFootnoteChildLink",
    "DocumentEventChildFootnoteChildLineBreak",
    "DocumentEventChildFootnoteChildText",
    "DocumentEventChildFootnoteChildToolCall",
    "DocumentEventChildFootnoteChildToolResult",
    "DocumentEventChildFootnoteChildTraceMessage",
    "DocumentEventChildHeading",
    "DocumentEventChildHeadingChild",
    "DocumentEventChildHeadingChildBlob",
    "DocumentEventChildHeadingChildCode",
    "DocumentEventChildHeadingChildComment",
    "DocumentEventChildHeadingChildDivider",
    "DocumentEventChildHeadingChildImage",
    "DocumentEventChildHeadingChildLink",
    "DocumentEventChildHeadingChildLineBreak",
    "DocumentEventChildHeadingChildText",
    "DocumentEventChildHeadingChildToolCall",
    "DocumentEventChildHeadingChildToolResult",
    "DocumentEventChildHeadingChildTraceMessage",
    "DocumentEventChildImage",
    "DocumentEventChildLink",
    "DocumentEventChildLineBreak",
    "DocumentEventChildList",
    "DocumentEventChildListItem",
    "DocumentEventChildListItemChild",
    "DocumentEventChildListItemChildBlob",
    "DocumentEventChildListItemChildCode",
    "DocumentEventChildListItemChildComment",
    "DocumentEventChildListItemChildDivider",
    "DocumentEventChildListItemChildImage",
    "DocumentEventChildListItemChildLink",
    "DocumentEventChildListItemChildLineBreak",
    "DocumentEventChildListItemChildText",
    "DocumentEventChildListItemChildToolCall",
    "DocumentEventChildListItemChildToolResult",
    "DocumentEventChildListItemChildTraceMessage",
    "DocumentEventChildParagraph",
    "DocumentEventChildParagraphChild",
    "DocumentEventChildParagraphChildBlob",
    "DocumentEventChildParagraphChildCode",
    "DocumentEventChildParagraphChildComment",
    "DocumentEventChildParagraphChildDivider",
    "DocumentEventChildParagraphChildImage",
    "DocumentEventChildParagraphChildLink",
    "DocumentEventChildParagraphChildLineBreak",
    "DocumentEventChildParagraphChildText",
    "DocumentEventChildParagraphChildToolCall",
    "DocumentEventChildParagraphChildToolResult",
    "DocumentEventChildParagraphChildTraceMessage",
    "DocumentEventChildQuote",
    "DocumentEventChildQuoteChild",
    "DocumentEventChildQuoteChildBlob",
    "DocumentEventChildQuoteChildCode",
    "DocumentEventChildQuoteChildComment",
    "DocumentEventChildQuoteChildDivider",
    "DocumentEventChildQuoteChildImage",
    "DocumentEventChildQuoteChildLink",
    "DocumentEventChildQuoteChildLineBreak",
    "DocumentEventChildQuoteChildText",
    "DocumentEventChildQuoteChildToolCall",
    "DocumentEventChildQuoteChildToolResult",
    "DocumentEventChildQuoteChildTraceMessage",
    "DocumentEventChildTable",
    "DocumentEventChildTableCell",
    "DocumentEventChildTableCellChild",
    "DocumentEventChildTableCellChildBlob",
    "DocumentEventChildTableCellChildCode",
    "DocumentEventChildTableCellChildComment",
    "DocumentEventChildTableCellChildDivider",
    "DocumentEventChildTableCellChildImage",
    "DocumentEventChildTableCellChildLink",
    "DocumentEventChildTableCellChildLineBreak",
    "DocumentEventChildTableCellChildText",
    "DocumentEventChildTableCellChildToolCall",
    "DocumentEventChildTableCellChildToolResult",
    "DocumentEventChildTableCellChildTraceMessage",
    "DocumentEventChildTableRow",
    "DocumentEventChildText",
    "DocumentEventChildToDo",
    "DocumentEventChildToDoChild",
    "DocumentEventChildToDoChildBlob",
    "DocumentEventChildToDoChildCode",
    "DocumentEventChildToDoChildComment",
    "DocumentEventChildToDoChildDivider",
    "DocumentEventChildToDoChildImage",
    "DocumentEventChildToDoChildLink",
    "DocumentEventChildToDoChildLineBreak",
    "DocumentEventChildToDoChildText",
    "DocumentEventChildToDoChildToolCall",
    "DocumentEventChildToDoChildToolResult",
    "DocumentEventChildToDoChildTraceMessage",
    "DocumentEventChildToolCall",
    "DocumentEventChildToolResult",
    "DocumentEventChildTraceMessage",
    "DocumentEventChildUtterance",
    "DocumentFile",
    "DocumentFileChild",
    "DocumentFileChildBlob",
    "DocumentFileChildCallout",
    "DocumentFileChildCalloutChild",
    "DocumentFileChildCalloutChildBlob",
    "DocumentFileChildCalloutChildCode",
    "DocumentFileChildCalloutChildComment",
    "DocumentFileChildCalloutChildDivider",
    "DocumentFileChildCalloutChildImage",
    "DocumentFileChildCalloutChildLink",
    "DocumentFileChildCalloutChildLineBreak",
    "DocumentFileChildCalloutChildText",
    "DocumentFileChildCalloutChildToolCall",
    "DocumentFileChildCalloutChildToolResult",
    "DocumentFileChildCalloutChildTraceMessage",
    "DocumentFileChildChunk",
    "DocumentFileChildChunkChild",
    "DocumentFileChildChunkChildBlob",
    "DocumentFileChildChunkChildCode",
    "DocumentFileChildChunkChildComment",
    "DocumentFileChildChunkChildDivider",
    "DocumentFileChildChunkChildImage",
    "DocumentFileChildChunkChildLink",
    "DocumentFileChildChunkChildLineBreak",
    "DocumentFileChildChunkChildText",
    "DocumentFileChildChunkChildToolCall",
    "DocumentFileChildChunkChildToolResult",
    "DocumentFileChildChunkChildTraceMessage",
    "DocumentFileChildCode",
    "DocumentFileChildComment",
    "DocumentFileChildDivider",
    "DocumentFileChildEquation",
    "DocumentFileChildEquationChild",
    "DocumentFileChildEquationChildBlob",
    "DocumentFileChildEquationChildCode",
    "DocumentFileChildEquationChildComment",
    "DocumentFileChildEquationChildDivider",
    "DocumentFileChildEquationChildImage",
    "DocumentFileChildEquationChildLink",
    "DocumentFileChildEquationChildLineBreak",
    "DocumentFileChildEquationChildText",
    "DocumentFileChildEquationChildToolCall",
    "DocumentFileChildEquationChildToolResult",
    "DocumentFileChildEquationChildTraceMessage",
    "DocumentFileChildFootnote",
    "DocumentFileChildFootnoteChild",
    "DocumentFileChildFootnoteChildBlob",
    "DocumentFileChildFootnoteChildCode",
    "DocumentFileChildFootnoteChildComment",
    "DocumentFileChildFootnoteChildDivider",
    "DocumentFileChildFootnoteChildImage",
    "DocumentFileChildFootnoteChildLink",
    "DocumentFileChildFootnoteChildLineBreak",
    "DocumentFileChildFootnoteChildText",
    "DocumentFileChildFootnoteChildToolCall",
    "DocumentFileChildFootnoteChildToolResult",
    "DocumentFileChildFootnoteChildTraceMessage",
    "DocumentFileChildHeading",
    "DocumentFileChildHeadingChild",
    "DocumentFileChildHeadingChildBlob",
    "DocumentFileChildHeadingChildCode",
    "DocumentFileChildHeadingChildComment",
    "DocumentFileChildHeadingChildDivider",
    "DocumentFileChildHeadingChildImage",
    "DocumentFileChildHeadingChildLink",
    "DocumentFileChildHeadingChildLineBreak",
    "DocumentFileChildHeadingChildText",
    "DocumentFileChildHeadingChildToolCall",
    "DocumentFileChildHeadingChildToolResult",
    "DocumentFileChildHeadingChildTraceMessage",
    "DocumentFileChildImage",
    "DocumentFileChildLink",
    "DocumentFileChildLineBreak",
    "DocumentFileChildList",
    "DocumentFileChildListItem",
    "DocumentFileChildListItemChild",
    "DocumentFileChildListItemChildBlob",
    "DocumentFileChildListItemChildCode",
    "DocumentFileChildListItemChildComment",
    "DocumentFileChildListItemChildDivider",
    "DocumentFileChildListItemChildImage",
    "DocumentFileChildListItemChildLink",
    "DocumentFileChildListItemChildLineBreak",
    "DocumentFileChildListItemChildText",
    "DocumentFileChildListItemChildToolCall",
    "DocumentFileChildListItemChildToolResult",
    "DocumentFileChildListItemChildTraceMessage",
    "DocumentFileChildParagraph",
    "DocumentFileChildParagraphChild",
    "DocumentFileChildParagraphChildBlob",
    "DocumentFileChildParagraphChildCode",
    "DocumentFileChildParagraphChildComment",
    "DocumentFileChildParagraphChildDivider",
    "DocumentFileChildParagraphChildImage",
    "DocumentFileChildParagraphChildLink",
    "DocumentFileChildParagraphChildLineBreak",
    "DocumentFileChildParagraphChildText",
    "DocumentFileChildParagraphChildToolCall",
    "DocumentFileChildParagraphChildToolResult",
    "DocumentFileChildParagraphChildTraceMessage",
    "DocumentFileChildQuote",
    "DocumentFileChildQuoteChild",
    "DocumentFileChildQuoteChildBlob",
    "DocumentFileChildQuoteChildCode",
    "DocumentFileChildQuoteChildComment",
    "DocumentFileChildQuoteChildDivider",
    "DocumentFileChildQuoteChildImage",
    "DocumentFileChildQuoteChildLink",
    "DocumentFileChildQuoteChildLineBreak",
    "DocumentFileChildQuoteChildText",
    "DocumentFileChildQuoteChildToolCall",
    "DocumentFileChildQuoteChildToolResult",
    "DocumentFileChildQuoteChildTraceMessage",
    "DocumentFileChildTable",
    "DocumentFileChildTableCell",
    "DocumentFileChildTableCellChild",
    "DocumentFileChildTableCellChildBlob",
    "DocumentFileChildTableCellChildCode",
    "DocumentFileChildTableCellChildComment",
    "DocumentFileChildTableCellChildDivider",
    "DocumentFileChildTableCellChildImage",
    "DocumentFileChildTableCellChildLink",
    "DocumentFileChildTableCellChildLineBreak",
    "DocumentFileChildTableCellChildText",
    "DocumentFileChildTableCellChildToolCall",
    "DocumentFileChildTableCellChildToolResult",
    "DocumentFileChildTableCellChildTraceMessage",
    "DocumentFileChildTableRow",
    "DocumentFileChildText",
    "DocumentFileChildToDo",
    "DocumentFileChildToDoChild",
    "DocumentFileChildToDoChildBlob",
    "DocumentFileChildToDoChildCode",
    "DocumentFileChildToDoChildComment",
    "DocumentFileChildToDoChildDivider",
    "DocumentFileChildToDoChildImage",
    "DocumentFileChildToDoChildLink",
    "DocumentFileChildToDoChildLineBreak",
    "DocumentFileChildToDoChildText",
    "DocumentFileChildToDoChildToolCall",
    "DocumentFileChildToDoChildToolResult",
    "DocumentFileChildToDoChildTraceMessage",
    "DocumentFileChildToolCall",
    "DocumentFileChildToolResult",
    "DocumentFileChildTraceMessage",
    "DocumentFileChildUtterance",
    "DocumentConversation",
    "DocumentConversationChild",
    "DocumentConversationChildSender",
    "DocumentConversationChildSenderChild",
    "DocumentConversationChildSenderChildBlob",
    "DocumentConversationChildSenderChildCode",
    "DocumentConversationChildSenderChildComment",
    "DocumentConversationChildSenderChildDivider",
    "DocumentConversationChildSenderChildImage",
    "DocumentConversationChildSenderChildLink",
    "DocumentConversationChildSenderChildLineBreak",
    "DocumentConversationChildSenderChildText",
    "DocumentConversationChildSenderChildToolCall",
    "DocumentConversationChildSenderChildToolResult",
    "DocumentConversationChildSenderChildTraceMessage",
    "DocumentConversationChildChild",
    "DocumentConversationChildChildBlob",
    "DocumentConversationChildChildCallout",
    "DocumentConversationChildChildCalloutChild",
    "DocumentConversationChildChildCalloutChildBlob",
    "DocumentConversationChildChildCalloutChildCode",
    "DocumentConversationChildChildCalloutChildComment",
    "DocumentConversationChildChildCalloutChildDivider",
    "DocumentConversationChildChildCalloutChildImage",
    "DocumentConversationChildChildCalloutChildLink",
    "DocumentConversationChildChildCalloutChildLineBreak",
    "DocumentConversationChildChildCalloutChildText",
    "DocumentConversationChildChildCalloutChildToolCall",
    "DocumentConversationChildChildCalloutChildToolResult",
    "DocumentConversationChildChildCalloutChildTraceMessage",
    "DocumentConversationChildChildChunk",
    "DocumentConversationChildChildChunkChild",
    "DocumentConversationChildChildChunkChildBlob",
    "DocumentConversationChildChildChunkChildCode",
    "DocumentConversationChildChildChunkChildComment",
    "DocumentConversationChildChildChunkChildDivider",
    "DocumentConversationChildChildChunkChildImage",
    "DocumentConversationChildChildChunkChildLink",
    "DocumentConversationChildChildChunkChildLineBreak",
    "DocumentConversationChildChildChunkChildText",
    "DocumentConversationChildChildChunkChildToolCall",
    "DocumentConversationChildChildChunkChildToolResult",
    "DocumentConversationChildChildChunkChildTraceMessage",
    "DocumentConversationChildChildCode",
    "DocumentConversationChildChildComment",
    "DocumentConversationChildChildDivider",
    "DocumentConversationChildChildEquation",
    "DocumentConversationChildChildEquationChild",
    "DocumentConversationChildChildEquationChildBlob",
    "DocumentConversationChildChildEquationChildCode",
    "DocumentConversationChildChildEquationChildComment",
    "DocumentConversationChildChildEquationChildDivider",
    "DocumentConversationChildChildEquationChildImage",
    "DocumentConversationChildChildEquationChildLink",
    "DocumentConversationChildChildEquationChildLineBreak",
    "DocumentConversationChildChildEquationChildText",
    "DocumentConversationChildChildEquationChildToolCall",
    "DocumentConversationChildChildEquationChildToolResult",
    "DocumentConversationChildChildEquationChildTraceMessage",
    "DocumentConversationChildChildFootnote",
    "DocumentConversationChildChildFootnoteChild",
    "DocumentConversationChildChildFootnoteChildBlob",
    "DocumentConversationChildChildFootnoteChildCode",
    "DocumentConversationChildChildFootnoteChildComment",
    "DocumentConversationChildChildFootnoteChildDivider",
    "DocumentConversationChildChildFootnoteChildImage",
    "DocumentConversationChildChildFootnoteChildLink",
    "DocumentConversationChildChildFootnoteChildLineBreak",
    "DocumentConversationChildChildFootnoteChildText",
    "DocumentConversationChildChildFootnoteChildToolCall",
    "DocumentConversationChildChildFootnoteChildToolResult",
    "DocumentConversationChildChildFootnoteChildTraceMessage",
    "DocumentConversationChildChildHeading",
    "DocumentConversationChildChildHeadingChild",
    "DocumentConversationChildChildHeadingChildBlob",
    "DocumentConversationChildChildHeadingChildCode",
    "DocumentConversationChildChildHeadingChildComment",
    "DocumentConversationChildChildHeadingChildDivider",
    "DocumentConversationChildChildHeadingChildImage",
    "DocumentConversationChildChildHeadingChildLink",
    "DocumentConversationChildChildHeadingChildLineBreak",
    "DocumentConversationChildChildHeadingChildText",
    "DocumentConversationChildChildHeadingChildToolCall",
    "DocumentConversationChildChildHeadingChildToolResult",
    "DocumentConversationChildChildHeadingChildTraceMessage",
    "DocumentConversationChildChildImage",
    "DocumentConversationChildChildLink",
    "DocumentConversationChildChildLineBreak",
    "DocumentConversationChildChildList",
    "DocumentConversationChildChildListItem",
    "DocumentConversationChildChildListItemChild",
    "DocumentConversationChildChildListItemChildBlob",
    "DocumentConversationChildChildListItemChildCode",
    "DocumentConversationChildChildListItemChildComment",
    "DocumentConversationChildChildListItemChildDivider",
    "DocumentConversationChildChildListItemChildImage",
    "DocumentConversationChildChildListItemChildLink",
    "DocumentConversationChildChildListItemChildLineBreak",
    "DocumentConversationChildChildListItemChildText",
    "DocumentConversationChildChildListItemChildToolCall",
    "DocumentConversationChildChildListItemChildToolResult",
    "DocumentConversationChildChildListItemChildTraceMessage",
    "DocumentConversationChildChildParagraph",
    "DocumentConversationChildChildParagraphChild",
    "DocumentConversationChildChildParagraphChildBlob",
    "DocumentConversationChildChildParagraphChildCode",
    "DocumentConversationChildChildParagraphChildComment",
    "DocumentConversationChildChildParagraphChildDivider",
    "DocumentConversationChildChildParagraphChildImage",
    "DocumentConversationChildChildParagraphChildLink",
    "DocumentConversationChildChildParagraphChildLineBreak",
    "DocumentConversationChildChildParagraphChildText",
    "DocumentConversationChildChildParagraphChildToolCall",
    "DocumentConversationChildChildParagraphChildToolResult",
    "DocumentConversationChildChildParagraphChildTraceMessage",
    "DocumentConversationChildChildQuote",
    "DocumentConversationChildChildQuoteChild",
    "DocumentConversationChildChildQuoteChildBlob",
    "DocumentConversationChildChildQuoteChildCode",
    "DocumentConversationChildChildQuoteChildComment",
    "DocumentConversationChildChildQuoteChildDivider",
    "DocumentConversationChildChildQuoteChildImage",
    "DocumentConversationChildChildQuoteChildLink",
    "DocumentConversationChildChildQuoteChildLineBreak",
    "DocumentConversationChildChildQuoteChildText",
    "DocumentConversationChildChildQuoteChildToolCall",
    "DocumentConversationChildChildQuoteChildToolResult",
    "DocumentConversationChildChildQuoteChildTraceMessage",
    "DocumentConversationChildChildTable",
    "DocumentConversationChildChildTableCell",
    "DocumentConversationChildChildTableCellChild",
    "DocumentConversationChildChildTableCellChildBlob",
    "DocumentConversationChildChildTableCellChildCode",
    "DocumentConversationChildChildTableCellChildComment",
    "DocumentConversationChildChildTableCellChildDivider",
    "DocumentConversationChildChildTableCellChildImage",
    "DocumentConversationChildChildTableCellChildLink",
    "DocumentConversationChildChildTableCellChildLineBreak",
    "DocumentConversationChildChildTableCellChildText",
    "DocumentConversationChildChildTableCellChildToolCall",
    "DocumentConversationChildChildTableCellChildToolResult",
    "DocumentConversationChildChildTableCellChildTraceMessage",
    "DocumentConversationChildChildTableRow",
    "DocumentConversationChildChildText",
    "DocumentConversationChildChildToDo",
    "DocumentConversationChildChildToDoChild",
    "DocumentConversationChildChildToDoChildBlob",
    "DocumentConversationChildChildToDoChildCode",
    "DocumentConversationChildChildToDoChildComment",
    "DocumentConversationChildChildToDoChildDivider",
    "DocumentConversationChildChildToDoChildImage",
    "DocumentConversationChildChildToDoChildLink",
    "DocumentConversationChildChildToDoChildLineBreak",
    "DocumentConversationChildChildToDoChildText",
    "DocumentConversationChildChildToDoChildToolCall",
    "DocumentConversationChildChildToDoChildToolResult",
    "DocumentConversationChildChildToDoChildTraceMessage",
    "DocumentConversationChildChildToolCall",
    "DocumentConversationChildChildToolResult",
    "DocumentConversationChildChildTraceMessage",
    "DocumentConversationChildChildUtterance",
    "DocumentConversationChildMentionedUser",
    "DocumentConversationChildMentionedUserChild",
    "DocumentConversationChildMentionedUserChildBlob",
    "DocumentConversationChildMentionedUserChildCode",
    "DocumentConversationChildMentionedUserChildComment",
    "DocumentConversationChildMentionedUserChildDivider",
    "DocumentConversationChildMentionedUserChildImage",
    "DocumentConversationChildMentionedUserChildLink",
    "DocumentConversationChildMentionedUserChildLineBreak",
    "DocumentConversationChildMentionedUserChildText",
    "DocumentConversationChildMentionedUserChildToolCall",
    "DocumentConversationChildMentionedUserChildToolResult",
    "DocumentConversationChildMentionedUserChildTraceMessage",
    "DocumentTrace",
    "DocumentTraceChild",
    "DocumentTraceChildTraceMessage",
    "DocumentTraceChildToolCall",
    "DocumentTraceChildToolResult",
    "DocumentTranscript",
    "DocumentTranscriptChild",
    "DocumentTranscriptParticipant",
    "DocumentTranscriptParticipantChild",
    "DocumentTranscriptParticipantChildBlob",
    "DocumentTranscriptParticipantChildCode",
    "DocumentTranscriptParticipantChildComment",
    "DocumentTranscriptParticipantChildDivider",
    "DocumentTranscriptParticipantChildImage",
    "DocumentTranscriptParticipantChildLink",
    "DocumentTranscriptParticipantChildLineBreak",
    "DocumentTranscriptParticipantChildText",
    "DocumentTranscriptParticipantChildToolCall",
    "DocumentTranscriptParticipantChildToolResult",
    "DocumentTranscriptParticipantChildTraceMessage",
    "DocumentCompany",
    "DocumentCompanyChild",
    "DocumentCompanyChildBlob",
    "DocumentCompanyChildCallout",
    "DocumentCompanyChildCalloutChild",
    "DocumentCompanyChildCalloutChildBlob",
    "DocumentCompanyChildCalloutChildCode",
    "DocumentCompanyChildCalloutChildComment",
    "DocumentCompanyChildCalloutChildDivider",
    "DocumentCompanyChildCalloutChildImage",
    "DocumentCompanyChildCalloutChildLink",
    "DocumentCompanyChildCalloutChildLineBreak",
    "DocumentCompanyChildCalloutChildText",
    "DocumentCompanyChildCalloutChildToolCall",
    "DocumentCompanyChildCalloutChildToolResult",
    "DocumentCompanyChildCalloutChildTraceMessage",
    "DocumentCompanyChildChunk",
    "DocumentCompanyChildChunkChild",
    "DocumentCompanyChildChunkChildBlob",
    "DocumentCompanyChildChunkChildCode",
    "DocumentCompanyChildChunkChildComment",
    "DocumentCompanyChildChunkChildDivider",
    "DocumentCompanyChildChunkChildImage",
    "DocumentCompanyChildChunkChildLink",
    "DocumentCompanyChildChunkChildLineBreak",
    "DocumentCompanyChildChunkChildText",
    "DocumentCompanyChildChunkChildToolCall",
    "DocumentCompanyChildChunkChildToolResult",
    "DocumentCompanyChildChunkChildTraceMessage",
    "DocumentCompanyChildCode",
    "DocumentCompanyChildComment",
    "DocumentCompanyChildDivider",
    "DocumentCompanyChildEquation",
    "DocumentCompanyChildEquationChild",
    "DocumentCompanyChildEquationChildBlob",
    "DocumentCompanyChildEquationChildCode",
    "DocumentCompanyChildEquationChildComment",
    "DocumentCompanyChildEquationChildDivider",
    "DocumentCompanyChildEquationChildImage",
    "DocumentCompanyChildEquationChildLink",
    "DocumentCompanyChildEquationChildLineBreak",
    "DocumentCompanyChildEquationChildText",
    "DocumentCompanyChildEquationChildToolCall",
    "DocumentCompanyChildEquationChildToolResult",
    "DocumentCompanyChildEquationChildTraceMessage",
    "DocumentCompanyChildFootnote",
    "DocumentCompanyChildFootnoteChild",
    "DocumentCompanyChildFootnoteChildBlob",
    "DocumentCompanyChildFootnoteChildCode",
    "DocumentCompanyChildFootnoteChildComment",
    "DocumentCompanyChildFootnoteChildDivider",
    "DocumentCompanyChildFootnoteChildImage",
    "DocumentCompanyChildFootnoteChildLink",
    "DocumentCompanyChildFootnoteChildLineBreak",
    "DocumentCompanyChildFootnoteChildText",
    "DocumentCompanyChildFootnoteChildToolCall",
    "DocumentCompanyChildFootnoteChildToolResult",
    "DocumentCompanyChildFootnoteChildTraceMessage",
    "DocumentCompanyChildHeading",
    "DocumentCompanyChildHeadingChild",
    "DocumentCompanyChildHeadingChildBlob",
    "DocumentCompanyChildHeadingChildCode",
    "DocumentCompanyChildHeadingChildComment",
    "DocumentCompanyChildHeadingChildDivider",
    "DocumentCompanyChildHeadingChildImage",
    "DocumentCompanyChildHeadingChildLink",
    "DocumentCompanyChildHeadingChildLineBreak",
    "DocumentCompanyChildHeadingChildText",
    "DocumentCompanyChildHeadingChildToolCall",
    "DocumentCompanyChildHeadingChildToolResult",
    "DocumentCompanyChildHeadingChildTraceMessage",
    "DocumentCompanyChildImage",
    "DocumentCompanyChildLink",
    "DocumentCompanyChildLineBreak",
    "DocumentCompanyChildList",
    "DocumentCompanyChildListItem",
    "DocumentCompanyChildListItemChild",
    "DocumentCompanyChildListItemChildBlob",
    "DocumentCompanyChildListItemChildCode",
    "DocumentCompanyChildListItemChildComment",
    "DocumentCompanyChildListItemChildDivider",
    "DocumentCompanyChildListItemChildImage",
    "DocumentCompanyChildListItemChildLink",
    "DocumentCompanyChildListItemChildLineBreak",
    "DocumentCompanyChildListItemChildText",
    "DocumentCompanyChildListItemChildToolCall",
    "DocumentCompanyChildListItemChildToolResult",
    "DocumentCompanyChildListItemChildTraceMessage",
    "DocumentCompanyChildParagraph",
    "DocumentCompanyChildParagraphChild",
    "DocumentCompanyChildParagraphChildBlob",
    "DocumentCompanyChildParagraphChildCode",
    "DocumentCompanyChildParagraphChildComment",
    "DocumentCompanyChildParagraphChildDivider",
    "DocumentCompanyChildParagraphChildImage",
    "DocumentCompanyChildParagraphChildLink",
    "DocumentCompanyChildParagraphChildLineBreak",
    "DocumentCompanyChildParagraphChildText",
    "DocumentCompanyChildParagraphChildToolCall",
    "DocumentCompanyChildParagraphChildToolResult",
    "DocumentCompanyChildParagraphChildTraceMessage",
    "DocumentCompanyChildQuote",
    "DocumentCompanyChildQuoteChild",
    "DocumentCompanyChildQuoteChildBlob",
    "DocumentCompanyChildQuoteChildCode",
    "DocumentCompanyChildQuoteChildComment",
    "DocumentCompanyChildQuoteChildDivider",
    "DocumentCompanyChildQuoteChildImage",
    "DocumentCompanyChildQuoteChildLink",
    "DocumentCompanyChildQuoteChildLineBreak",
    "DocumentCompanyChildQuoteChildText",
    "DocumentCompanyChildQuoteChildToolCall",
    "DocumentCompanyChildQuoteChildToolResult",
    "DocumentCompanyChildQuoteChildTraceMessage",
    "DocumentCompanyChildTable",
    "DocumentCompanyChildTableCell",
    "DocumentCompanyChildTableCellChild",
    "DocumentCompanyChildTableCellChildBlob",
    "DocumentCompanyChildTableCellChildCode",
    "DocumentCompanyChildTableCellChildComment",
    "DocumentCompanyChildTableCellChildDivider",
    "DocumentCompanyChildTableCellChildImage",
    "DocumentCompanyChildTableCellChildLink",
    "DocumentCompanyChildTableCellChildLineBreak",
    "DocumentCompanyChildTableCellChildText",
    "DocumentCompanyChildTableCellChildToolCall",
    "DocumentCompanyChildTableCellChildToolResult",
    "DocumentCompanyChildTableCellChildTraceMessage",
    "DocumentCompanyChildTableRow",
    "DocumentCompanyChildText",
    "DocumentCompanyChildToDo",
    "DocumentCompanyChildToDoChild",
    "DocumentCompanyChildToDoChildBlob",
    "DocumentCompanyChildToDoChildCode",
    "DocumentCompanyChildToDoChildComment",
    "DocumentCompanyChildToDoChildDivider",
    "DocumentCompanyChildToDoChildImage",
    "DocumentCompanyChildToDoChildLink",
    "DocumentCompanyChildToDoChildLineBreak",
    "DocumentCompanyChildToDoChildText",
    "DocumentCompanyChildToDoChildToolCall",
    "DocumentCompanyChildToDoChildToolResult",
    "DocumentCompanyChildToDoChildTraceMessage",
    "DocumentCompanyChildToolCall",
    "DocumentCompanyChildToolResult",
    "DocumentCompanyChildTraceMessage",
    "DocumentCompanyChildUtterance",
    "DocumentDeal",
    "DocumentDealChild",
    "DocumentDealChildBlob",
    "DocumentDealChildCallout",
    "DocumentDealChildCalloutChild",
    "DocumentDealChildCalloutChildBlob",
    "DocumentDealChildCalloutChildCode",
    "DocumentDealChildCalloutChildComment",
    "DocumentDealChildCalloutChildDivider",
    "DocumentDealChildCalloutChildImage",
    "DocumentDealChildCalloutChildLink",
    "DocumentDealChildCalloutChildLineBreak",
    "DocumentDealChildCalloutChildText",
    "DocumentDealChildCalloutChildToolCall",
    "DocumentDealChildCalloutChildToolResult",
    "DocumentDealChildCalloutChildTraceMessage",
    "DocumentDealChildChunk",
    "DocumentDealChildChunkChild",
    "DocumentDealChildChunkChildBlob",
    "DocumentDealChildChunkChildCode",
    "DocumentDealChildChunkChildComment",
    "DocumentDealChildChunkChildDivider",
    "DocumentDealChildChunkChildImage",
    "DocumentDealChildChunkChildLink",
    "DocumentDealChildChunkChildLineBreak",
    "DocumentDealChildChunkChildText",
    "DocumentDealChildChunkChildToolCall",
    "DocumentDealChildChunkChildToolResult",
    "DocumentDealChildChunkChildTraceMessage",
    "DocumentDealChildCode",
    "DocumentDealChildComment",
    "DocumentDealChildDivider",
    "DocumentDealChildEquation",
    "DocumentDealChildEquationChild",
    "DocumentDealChildEquationChildBlob",
    "DocumentDealChildEquationChildCode",
    "DocumentDealChildEquationChildComment",
    "DocumentDealChildEquationChildDivider",
    "DocumentDealChildEquationChildImage",
    "DocumentDealChildEquationChildLink",
    "DocumentDealChildEquationChildLineBreak",
    "DocumentDealChildEquationChildText",
    "DocumentDealChildEquationChildToolCall",
    "DocumentDealChildEquationChildToolResult",
    "DocumentDealChildEquationChildTraceMessage",
    "DocumentDealChildFootnote",
    "DocumentDealChildFootnoteChild",
    "DocumentDealChildFootnoteChildBlob",
    "DocumentDealChildFootnoteChildCode",
    "DocumentDealChildFootnoteChildComment",
    "DocumentDealChildFootnoteChildDivider",
    "DocumentDealChildFootnoteChildImage",
    "DocumentDealChildFootnoteChildLink",
    "DocumentDealChildFootnoteChildLineBreak",
    "DocumentDealChildFootnoteChildText",
    "DocumentDealChildFootnoteChildToolCall",
    "DocumentDealChildFootnoteChildToolResult",
    "DocumentDealChildFootnoteChildTraceMessage",
    "DocumentDealChildHeading",
    "DocumentDealChildHeadingChild",
    "DocumentDealChildHeadingChildBlob",
    "DocumentDealChildHeadingChildCode",
    "DocumentDealChildHeadingChildComment",
    "DocumentDealChildHeadingChildDivider",
    "DocumentDealChildHeadingChildImage",
    "DocumentDealChildHeadingChildLink",
    "DocumentDealChildHeadingChildLineBreak",
    "DocumentDealChildHeadingChildText",
    "DocumentDealChildHeadingChildToolCall",
    "DocumentDealChildHeadingChildToolResult",
    "DocumentDealChildHeadingChildTraceMessage",
    "DocumentDealChildImage",
    "DocumentDealChildLink",
    "DocumentDealChildLineBreak",
    "DocumentDealChildList",
    "DocumentDealChildListItem",
    "DocumentDealChildListItemChild",
    "DocumentDealChildListItemChildBlob",
    "DocumentDealChildListItemChildCode",
    "DocumentDealChildListItemChildComment",
    "DocumentDealChildListItemChildDivider",
    "DocumentDealChildListItemChildImage",
    "DocumentDealChildListItemChildLink",
    "DocumentDealChildListItemChildLineBreak",
    "DocumentDealChildListItemChildText",
    "DocumentDealChildListItemChildToolCall",
    "DocumentDealChildListItemChildToolResult",
    "DocumentDealChildListItemChildTraceMessage",
    "DocumentDealChildParagraph",
    "DocumentDealChildParagraphChild",
    "DocumentDealChildParagraphChildBlob",
    "DocumentDealChildParagraphChildCode",
    "DocumentDealChildParagraphChildComment",
    "DocumentDealChildParagraphChildDivider",
    "DocumentDealChildParagraphChildImage",
    "DocumentDealChildParagraphChildLink",
    "DocumentDealChildParagraphChildLineBreak",
    "DocumentDealChildParagraphChildText",
    "DocumentDealChildParagraphChildToolCall",
    "DocumentDealChildParagraphChildToolResult",
    "DocumentDealChildParagraphChildTraceMessage",
    "DocumentDealChildQuote",
    "DocumentDealChildQuoteChild",
    "DocumentDealChildQuoteChildBlob",
    "DocumentDealChildQuoteChildCode",
    "DocumentDealChildQuoteChildComment",
    "DocumentDealChildQuoteChildDivider",
    "DocumentDealChildQuoteChildImage",
    "DocumentDealChildQuoteChildLink",
    "DocumentDealChildQuoteChildLineBreak",
    "DocumentDealChildQuoteChildText",
    "DocumentDealChildQuoteChildToolCall",
    "DocumentDealChildQuoteChildToolResult",
    "DocumentDealChildQuoteChildTraceMessage",
    "DocumentDealChildTable",
    "DocumentDealChildTableCell",
    "DocumentDealChildTableCellChild",
    "DocumentDealChildTableCellChildBlob",
    "DocumentDealChildTableCellChildCode",
    "DocumentDealChildTableCellChildComment",
    "DocumentDealChildTableCellChildDivider",
    "DocumentDealChildTableCellChildImage",
    "DocumentDealChildTableCellChildLink",
    "DocumentDealChildTableCellChildLineBreak",
    "DocumentDealChildTableCellChildText",
    "DocumentDealChildTableCellChildToolCall",
    "DocumentDealChildTableCellChildToolResult",
    "DocumentDealChildTableCellChildTraceMessage",
    "DocumentDealChildTableRow",
    "DocumentDealChildText",
    "DocumentDealChildToDo",
    "DocumentDealChildToDoChild",
    "DocumentDealChildToDoChildBlob",
    "DocumentDealChildToDoChildCode",
    "DocumentDealChildToDoChildComment",
    "DocumentDealChildToDoChildDivider",
    "DocumentDealChildToDoChildImage",
    "DocumentDealChildToDoChildLink",
    "DocumentDealChildToDoChildLineBreak",
    "DocumentDealChildToDoChildText",
    "DocumentDealChildToDoChildToolCall",
    "DocumentDealChildToDoChildToolResult",
    "DocumentDealChildToDoChildTraceMessage",
    "DocumentDealChildToolCall",
    "DocumentDealChildToolResult",
    "DocumentDealChildTraceMessage",
    "DocumentDealChildUtterance",
]


class DocumentDocumentChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildCalloutChild: TypeAlias = Union[
    DocumentDocumentChildCalloutChildBlob,
    DocumentDocumentChildCalloutChildCode,
    DocumentDocumentChildCalloutChildComment,
    DocumentDocumentChildCalloutChildDivider,
    DocumentDocumentChildCalloutChildImage,
    DocumentDocumentChildCalloutChildLink,
    DocumentDocumentChildCalloutChildLineBreak,
    DocumentDocumentChildCalloutChildText,
    DocumentDocumentChildCalloutChildToolCall,
    DocumentDocumentChildCalloutChildToolResult,
    DocumentDocumentChildCalloutChildTraceMessage,
    object,
]


class DocumentDocumentChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDocumentChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentDocumentChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildChunkChild: TypeAlias = Union[
    DocumentDocumentChildChunkChildBlob,
    DocumentDocumentChildChunkChildCode,
    DocumentDocumentChildChunkChildComment,
    DocumentDocumentChildChunkChildDivider,
    DocumentDocumentChildChunkChildImage,
    DocumentDocumentChildChunkChildLink,
    DocumentDocumentChildChunkChildLineBreak,
    DocumentDocumentChildChunkChildText,
    DocumentDocumentChildChunkChildToolCall,
    DocumentDocumentChildChunkChildToolResult,
    DocumentDocumentChildChunkChildTraceMessage,
    object,
]


class DocumentDocumentChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDocumentChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentDocumentChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildEquationChild: TypeAlias = Union[
    DocumentDocumentChildEquationChildBlob,
    DocumentDocumentChildEquationChildCode,
    DocumentDocumentChildEquationChildComment,
    DocumentDocumentChildEquationChildDivider,
    DocumentDocumentChildEquationChildImage,
    DocumentDocumentChildEquationChildLink,
    DocumentDocumentChildEquationChildLineBreak,
    DocumentDocumentChildEquationChildText,
    DocumentDocumentChildEquationChildToolCall,
    DocumentDocumentChildEquationChildToolResult,
    DocumentDocumentChildEquationChildTraceMessage,
    object,
]


class DocumentDocumentChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDocumentChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentDocumentChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildFootnoteChild: TypeAlias = Union[
    DocumentDocumentChildFootnoteChildBlob,
    DocumentDocumentChildFootnoteChildCode,
    DocumentDocumentChildFootnoteChildComment,
    DocumentDocumentChildFootnoteChildDivider,
    DocumentDocumentChildFootnoteChildImage,
    DocumentDocumentChildFootnoteChildLink,
    DocumentDocumentChildFootnoteChildLineBreak,
    DocumentDocumentChildFootnoteChildText,
    DocumentDocumentChildFootnoteChildToolCall,
    DocumentDocumentChildFootnoteChildToolResult,
    DocumentDocumentChildFootnoteChildTraceMessage,
    object,
]


class DocumentDocumentChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDocumentChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentDocumentChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildHeadingChild: TypeAlias = Union[
    DocumentDocumentChildHeadingChildBlob,
    DocumentDocumentChildHeadingChildCode,
    DocumentDocumentChildHeadingChildComment,
    DocumentDocumentChildHeadingChildDivider,
    DocumentDocumentChildHeadingChildImage,
    DocumentDocumentChildHeadingChildLink,
    DocumentDocumentChildHeadingChildLineBreak,
    DocumentDocumentChildHeadingChildText,
    DocumentDocumentChildHeadingChildToolCall,
    DocumentDocumentChildHeadingChildToolResult,
    DocumentDocumentChildHeadingChildTraceMessage,
    object,
]


class DocumentDocumentChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentDocumentChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentDocumentChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentDocumentChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildListItemChild: TypeAlias = Union[
    DocumentDocumentChildListItemChildBlob,
    DocumentDocumentChildListItemChildCode,
    DocumentDocumentChildListItemChildComment,
    DocumentDocumentChildListItemChildDivider,
    DocumentDocumentChildListItemChildImage,
    DocumentDocumentChildListItemChildLink,
    DocumentDocumentChildListItemChildLineBreak,
    DocumentDocumentChildListItemChildText,
    DocumentDocumentChildListItemChildToolCall,
    DocumentDocumentChildListItemChildToolResult,
    DocumentDocumentChildListItemChildTraceMessage,
    object,
]


class DocumentDocumentChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDocumentChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentDocumentChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildParagraphChild: TypeAlias = Union[
    DocumentDocumentChildParagraphChildBlob,
    DocumentDocumentChildParagraphChildCode,
    DocumentDocumentChildParagraphChildComment,
    DocumentDocumentChildParagraphChildDivider,
    DocumentDocumentChildParagraphChildImage,
    DocumentDocumentChildParagraphChildLink,
    DocumentDocumentChildParagraphChildLineBreak,
    DocumentDocumentChildParagraphChildText,
    DocumentDocumentChildParagraphChildToolCall,
    DocumentDocumentChildParagraphChildToolResult,
    DocumentDocumentChildParagraphChildTraceMessage,
    object,
]


class DocumentDocumentChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDocumentChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentDocumentChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildQuoteChild: TypeAlias = Union[
    DocumentDocumentChildQuoteChildBlob,
    DocumentDocumentChildQuoteChildCode,
    DocumentDocumentChildQuoteChildComment,
    DocumentDocumentChildQuoteChildDivider,
    DocumentDocumentChildQuoteChildImage,
    DocumentDocumentChildQuoteChildLink,
    DocumentDocumentChildQuoteChildLineBreak,
    DocumentDocumentChildQuoteChildText,
    DocumentDocumentChildQuoteChildToolCall,
    DocumentDocumentChildQuoteChildToolResult,
    DocumentDocumentChildQuoteChildTraceMessage,
    object,
]


class DocumentDocumentChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDocumentChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentDocumentChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentDocumentChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildTableCellChild: TypeAlias = Union[
    DocumentDocumentChildTableCellChildBlob,
    DocumentDocumentChildTableCellChildCode,
    DocumentDocumentChildTableCellChildComment,
    DocumentDocumentChildTableCellChildDivider,
    DocumentDocumentChildTableCellChildImage,
    DocumentDocumentChildTableCellChildLink,
    DocumentDocumentChildTableCellChildLineBreak,
    DocumentDocumentChildTableCellChildText,
    DocumentDocumentChildTableCellChildToolCall,
    DocumentDocumentChildTableCellChildToolResult,
    DocumentDocumentChildTableCellChildTraceMessage,
    object,
]


class DocumentDocumentChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentDocumentChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentDocumentChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentDocumentChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDocumentChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDocumentChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDocumentChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDocumentChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDocumentChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDocumentChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDocumentChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDocumentChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDocumentChildToDoChild: TypeAlias = Union[
    DocumentDocumentChildToDoChildBlob,
    DocumentDocumentChildToDoChildCode,
    DocumentDocumentChildToDoChildComment,
    DocumentDocumentChildToDoChildDivider,
    DocumentDocumentChildToDoChildImage,
    DocumentDocumentChildToDoChildLink,
    DocumentDocumentChildToDoChildLineBreak,
    DocumentDocumentChildToDoChildText,
    DocumentDocumentChildToDoChildToolCall,
    DocumentDocumentChildToDoChildToolResult,
    DocumentDocumentChildToDoChildTraceMessage,
    object,
]


class DocumentDocumentChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentDocumentChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentDocumentChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDocumentChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDocumentChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentDocumentChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentDocumentChild: TypeAlias = Annotated[
    Union[
        DocumentDocumentChildBlob,
        DocumentDocumentChildCallout,
        DocumentDocumentChildChunk,
        DocumentDocumentChildCode,
        DocumentDocumentChildComment,
        DocumentDocumentChildDivider,
        DocumentDocumentChildEquation,
        DocumentDocumentChildFootnote,
        DocumentDocumentChildHeading,
        DocumentDocumentChildImage,
        DocumentDocumentChildLink,
        DocumentDocumentChildLineBreak,
        DocumentDocumentChildList,
        DocumentDocumentChildListItem,
        DocumentDocumentChildParagraph,
        DocumentDocumentChildQuote,
        DocumentDocumentChildTable,
        DocumentDocumentChildTableCell,
        DocumentDocumentChildTableRow,
        DocumentDocumentChildText,
        DocumentDocumentChildToDo,
        DocumentDocumentChildToolCall,
        DocumentDocumentChildToolResult,
        DocumentDocumentChildTraceMessage,
        DocumentDocumentChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentDocument(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDocumentChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["document"]] = None


class DocumentWebsiteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildCalloutChild: TypeAlias = Union[
    DocumentWebsiteChildCalloutChildBlob,
    DocumentWebsiteChildCalloutChildCode,
    DocumentWebsiteChildCalloutChildComment,
    DocumentWebsiteChildCalloutChildDivider,
    DocumentWebsiteChildCalloutChildImage,
    DocumentWebsiteChildCalloutChildLink,
    DocumentWebsiteChildCalloutChildLineBreak,
    DocumentWebsiteChildCalloutChildText,
    DocumentWebsiteChildCalloutChildToolCall,
    DocumentWebsiteChildCalloutChildToolResult,
    DocumentWebsiteChildCalloutChildTraceMessage,
    object,
]


class DocumentWebsiteChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentWebsiteChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentWebsiteChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildChunkChild: TypeAlias = Union[
    DocumentWebsiteChildChunkChildBlob,
    DocumentWebsiteChildChunkChildCode,
    DocumentWebsiteChildChunkChildComment,
    DocumentWebsiteChildChunkChildDivider,
    DocumentWebsiteChildChunkChildImage,
    DocumentWebsiteChildChunkChildLink,
    DocumentWebsiteChildChunkChildLineBreak,
    DocumentWebsiteChildChunkChildText,
    DocumentWebsiteChildChunkChildToolCall,
    DocumentWebsiteChildChunkChildToolResult,
    DocumentWebsiteChildChunkChildTraceMessage,
    object,
]


class DocumentWebsiteChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentWebsiteChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentWebsiteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildEquationChild: TypeAlias = Union[
    DocumentWebsiteChildEquationChildBlob,
    DocumentWebsiteChildEquationChildCode,
    DocumentWebsiteChildEquationChildComment,
    DocumentWebsiteChildEquationChildDivider,
    DocumentWebsiteChildEquationChildImage,
    DocumentWebsiteChildEquationChildLink,
    DocumentWebsiteChildEquationChildLineBreak,
    DocumentWebsiteChildEquationChildText,
    DocumentWebsiteChildEquationChildToolCall,
    DocumentWebsiteChildEquationChildToolResult,
    DocumentWebsiteChildEquationChildTraceMessage,
    object,
]


class DocumentWebsiteChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentWebsiteChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentWebsiteChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildFootnoteChild: TypeAlias = Union[
    DocumentWebsiteChildFootnoteChildBlob,
    DocumentWebsiteChildFootnoteChildCode,
    DocumentWebsiteChildFootnoteChildComment,
    DocumentWebsiteChildFootnoteChildDivider,
    DocumentWebsiteChildFootnoteChildImage,
    DocumentWebsiteChildFootnoteChildLink,
    DocumentWebsiteChildFootnoteChildLineBreak,
    DocumentWebsiteChildFootnoteChildText,
    DocumentWebsiteChildFootnoteChildToolCall,
    DocumentWebsiteChildFootnoteChildToolResult,
    DocumentWebsiteChildFootnoteChildTraceMessage,
    object,
]


class DocumentWebsiteChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentWebsiteChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentWebsiteChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildHeadingChild: TypeAlias = Union[
    DocumentWebsiteChildHeadingChildBlob,
    DocumentWebsiteChildHeadingChildCode,
    DocumentWebsiteChildHeadingChildComment,
    DocumentWebsiteChildHeadingChildDivider,
    DocumentWebsiteChildHeadingChildImage,
    DocumentWebsiteChildHeadingChildLink,
    DocumentWebsiteChildHeadingChildLineBreak,
    DocumentWebsiteChildHeadingChildText,
    DocumentWebsiteChildHeadingChildToolCall,
    DocumentWebsiteChildHeadingChildToolResult,
    DocumentWebsiteChildHeadingChildTraceMessage,
    object,
]


class DocumentWebsiteChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentWebsiteChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentWebsiteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentWebsiteChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildListItemChild: TypeAlias = Union[
    DocumentWebsiteChildListItemChildBlob,
    DocumentWebsiteChildListItemChildCode,
    DocumentWebsiteChildListItemChildComment,
    DocumentWebsiteChildListItemChildDivider,
    DocumentWebsiteChildListItemChildImage,
    DocumentWebsiteChildListItemChildLink,
    DocumentWebsiteChildListItemChildLineBreak,
    DocumentWebsiteChildListItemChildText,
    DocumentWebsiteChildListItemChildToolCall,
    DocumentWebsiteChildListItemChildToolResult,
    DocumentWebsiteChildListItemChildTraceMessage,
    object,
]


class DocumentWebsiteChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentWebsiteChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentWebsiteChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildParagraphChild: TypeAlias = Union[
    DocumentWebsiteChildParagraphChildBlob,
    DocumentWebsiteChildParagraphChildCode,
    DocumentWebsiteChildParagraphChildComment,
    DocumentWebsiteChildParagraphChildDivider,
    DocumentWebsiteChildParagraphChildImage,
    DocumentWebsiteChildParagraphChildLink,
    DocumentWebsiteChildParagraphChildLineBreak,
    DocumentWebsiteChildParagraphChildText,
    DocumentWebsiteChildParagraphChildToolCall,
    DocumentWebsiteChildParagraphChildToolResult,
    DocumentWebsiteChildParagraphChildTraceMessage,
    object,
]


class DocumentWebsiteChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentWebsiteChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentWebsiteChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildQuoteChild: TypeAlias = Union[
    DocumentWebsiteChildQuoteChildBlob,
    DocumentWebsiteChildQuoteChildCode,
    DocumentWebsiteChildQuoteChildComment,
    DocumentWebsiteChildQuoteChildDivider,
    DocumentWebsiteChildQuoteChildImage,
    DocumentWebsiteChildQuoteChildLink,
    DocumentWebsiteChildQuoteChildLineBreak,
    DocumentWebsiteChildQuoteChildText,
    DocumentWebsiteChildQuoteChildToolCall,
    DocumentWebsiteChildQuoteChildToolResult,
    DocumentWebsiteChildQuoteChildTraceMessage,
    object,
]


class DocumentWebsiteChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentWebsiteChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentWebsiteChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentWebsiteChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildTableCellChild: TypeAlias = Union[
    DocumentWebsiteChildTableCellChildBlob,
    DocumentWebsiteChildTableCellChildCode,
    DocumentWebsiteChildTableCellChildComment,
    DocumentWebsiteChildTableCellChildDivider,
    DocumentWebsiteChildTableCellChildImage,
    DocumentWebsiteChildTableCellChildLink,
    DocumentWebsiteChildTableCellChildLineBreak,
    DocumentWebsiteChildTableCellChildText,
    DocumentWebsiteChildTableCellChildToolCall,
    DocumentWebsiteChildTableCellChildToolResult,
    DocumentWebsiteChildTableCellChildTraceMessage,
    object,
]


class DocumentWebsiteChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentWebsiteChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentWebsiteChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentWebsiteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentWebsiteChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentWebsiteChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentWebsiteChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentWebsiteChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentWebsiteChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentWebsiteChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentWebsiteChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentWebsiteChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentWebsiteChildToDoChild: TypeAlias = Union[
    DocumentWebsiteChildToDoChildBlob,
    DocumentWebsiteChildToDoChildCode,
    DocumentWebsiteChildToDoChildComment,
    DocumentWebsiteChildToDoChildDivider,
    DocumentWebsiteChildToDoChildImage,
    DocumentWebsiteChildToDoChildLink,
    DocumentWebsiteChildToDoChildLineBreak,
    DocumentWebsiteChildToDoChildText,
    DocumentWebsiteChildToDoChildToolCall,
    DocumentWebsiteChildToDoChildToolResult,
    DocumentWebsiteChildToDoChildTraceMessage,
    object,
]


class DocumentWebsiteChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentWebsiteChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentWebsiteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentWebsiteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentWebsiteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentWebsiteChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentWebsiteChild: TypeAlias = Annotated[
    Union[
        DocumentWebsiteChildBlob,
        DocumentWebsiteChildCallout,
        DocumentWebsiteChildChunk,
        DocumentWebsiteChildCode,
        DocumentWebsiteChildComment,
        DocumentWebsiteChildDivider,
        DocumentWebsiteChildEquation,
        DocumentWebsiteChildFootnote,
        DocumentWebsiteChildHeading,
        DocumentWebsiteChildImage,
        DocumentWebsiteChildLink,
        DocumentWebsiteChildLineBreak,
        DocumentWebsiteChildList,
        DocumentWebsiteChildListItem,
        DocumentWebsiteChildParagraph,
        DocumentWebsiteChildQuote,
        DocumentWebsiteChildTable,
        DocumentWebsiteChildTableCell,
        DocumentWebsiteChildTableRow,
        DocumentWebsiteChildText,
        DocumentWebsiteChildToDo,
        DocumentWebsiteChildToolCall,
        DocumentWebsiteChildToolResult,
        DocumentWebsiteChildTraceMessage,
        DocumentWebsiteChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentWebsite(BaseModel):
    url: str

    id: Optional[str] = None

    children: Optional[List[DocumentWebsiteChild]] = None

    description: Optional[str] = None

    favicon: Optional[str] = None

    image_url: Optional[str] = None

    language: Optional[str] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["website"]] = None


class DocumentTaskChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildCalloutChild: TypeAlias = Union[
    DocumentTaskChildCalloutChildBlob,
    DocumentTaskChildCalloutChildCode,
    DocumentTaskChildCalloutChildComment,
    DocumentTaskChildCalloutChildDivider,
    DocumentTaskChildCalloutChildImage,
    DocumentTaskChildCalloutChildLink,
    DocumentTaskChildCalloutChildLineBreak,
    DocumentTaskChildCalloutChildText,
    DocumentTaskChildCalloutChildToolCall,
    DocumentTaskChildCalloutChildToolResult,
    DocumentTaskChildCalloutChildTraceMessage,
    object,
]


class DocumentTaskChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentTaskChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildChunkChild: TypeAlias = Union[
    DocumentTaskChildChunkChildBlob,
    DocumentTaskChildChunkChildCode,
    DocumentTaskChildChunkChildComment,
    DocumentTaskChildChunkChildDivider,
    DocumentTaskChildChunkChildImage,
    DocumentTaskChildChunkChildLink,
    DocumentTaskChildChunkChildLineBreak,
    DocumentTaskChildChunkChildText,
    DocumentTaskChildChunkChildToolCall,
    DocumentTaskChildChunkChildToolResult,
    DocumentTaskChildChunkChildTraceMessage,
    object,
]


class DocumentTaskChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentTaskChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildEquationChild: TypeAlias = Union[
    DocumentTaskChildEquationChildBlob,
    DocumentTaskChildEquationChildCode,
    DocumentTaskChildEquationChildComment,
    DocumentTaskChildEquationChildDivider,
    DocumentTaskChildEquationChildImage,
    DocumentTaskChildEquationChildLink,
    DocumentTaskChildEquationChildLineBreak,
    DocumentTaskChildEquationChildText,
    DocumentTaskChildEquationChildToolCall,
    DocumentTaskChildEquationChildToolResult,
    DocumentTaskChildEquationChildTraceMessage,
    object,
]


class DocumentTaskChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentTaskChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildFootnoteChild: TypeAlias = Union[
    DocumentTaskChildFootnoteChildBlob,
    DocumentTaskChildFootnoteChildCode,
    DocumentTaskChildFootnoteChildComment,
    DocumentTaskChildFootnoteChildDivider,
    DocumentTaskChildFootnoteChildImage,
    DocumentTaskChildFootnoteChildLink,
    DocumentTaskChildFootnoteChildLineBreak,
    DocumentTaskChildFootnoteChildText,
    DocumentTaskChildFootnoteChildToolCall,
    DocumentTaskChildFootnoteChildToolResult,
    DocumentTaskChildFootnoteChildTraceMessage,
    object,
]


class DocumentTaskChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentTaskChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildHeadingChild: TypeAlias = Union[
    DocumentTaskChildHeadingChildBlob,
    DocumentTaskChildHeadingChildCode,
    DocumentTaskChildHeadingChildComment,
    DocumentTaskChildHeadingChildDivider,
    DocumentTaskChildHeadingChildImage,
    DocumentTaskChildHeadingChildLink,
    DocumentTaskChildHeadingChildLineBreak,
    DocumentTaskChildHeadingChildText,
    DocumentTaskChildHeadingChildToolCall,
    DocumentTaskChildHeadingChildToolResult,
    DocumentTaskChildHeadingChildTraceMessage,
    object,
]


class DocumentTaskChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentTaskChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentTaskChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentTaskChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildListItemChild: TypeAlias = Union[
    DocumentTaskChildListItemChildBlob,
    DocumentTaskChildListItemChildCode,
    DocumentTaskChildListItemChildComment,
    DocumentTaskChildListItemChildDivider,
    DocumentTaskChildListItemChildImage,
    DocumentTaskChildListItemChildLink,
    DocumentTaskChildListItemChildLineBreak,
    DocumentTaskChildListItemChildText,
    DocumentTaskChildListItemChildToolCall,
    DocumentTaskChildListItemChildToolResult,
    DocumentTaskChildListItemChildTraceMessage,
    object,
]


class DocumentTaskChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentTaskChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildParagraphChild: TypeAlias = Union[
    DocumentTaskChildParagraphChildBlob,
    DocumentTaskChildParagraphChildCode,
    DocumentTaskChildParagraphChildComment,
    DocumentTaskChildParagraphChildDivider,
    DocumentTaskChildParagraphChildImage,
    DocumentTaskChildParagraphChildLink,
    DocumentTaskChildParagraphChildLineBreak,
    DocumentTaskChildParagraphChildText,
    DocumentTaskChildParagraphChildToolCall,
    DocumentTaskChildParagraphChildToolResult,
    DocumentTaskChildParagraphChildTraceMessage,
    object,
]


class DocumentTaskChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentTaskChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildQuoteChild: TypeAlias = Union[
    DocumentTaskChildQuoteChildBlob,
    DocumentTaskChildQuoteChildCode,
    DocumentTaskChildQuoteChildComment,
    DocumentTaskChildQuoteChildDivider,
    DocumentTaskChildQuoteChildImage,
    DocumentTaskChildQuoteChildLink,
    DocumentTaskChildQuoteChildLineBreak,
    DocumentTaskChildQuoteChildText,
    DocumentTaskChildQuoteChildToolCall,
    DocumentTaskChildQuoteChildToolResult,
    DocumentTaskChildQuoteChildTraceMessage,
    object,
]


class DocumentTaskChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentTaskChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentTaskChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildTableCellChild: TypeAlias = Union[
    DocumentTaskChildTableCellChildBlob,
    DocumentTaskChildTableCellChildCode,
    DocumentTaskChildTableCellChildComment,
    DocumentTaskChildTableCellChildDivider,
    DocumentTaskChildTableCellChildImage,
    DocumentTaskChildTableCellChildLink,
    DocumentTaskChildTableCellChildLineBreak,
    DocumentTaskChildTableCellChildText,
    DocumentTaskChildTableCellChildToolCall,
    DocumentTaskChildTableCellChildToolResult,
    DocumentTaskChildTableCellChildTraceMessage,
    object,
]


class DocumentTaskChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentTaskChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentTaskChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentTaskChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskChildToDoChild: TypeAlias = Union[
    DocumentTaskChildToDoChildBlob,
    DocumentTaskChildToDoChildCode,
    DocumentTaskChildToDoChildComment,
    DocumentTaskChildToDoChildDivider,
    DocumentTaskChildToDoChildImage,
    DocumentTaskChildToDoChildLink,
    DocumentTaskChildToDoChildLineBreak,
    DocumentTaskChildToDoChildText,
    DocumentTaskChildToDoChildToolCall,
    DocumentTaskChildToDoChildToolResult,
    DocumentTaskChildToDoChildTraceMessage,
    object,
]


class DocumentTaskChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentTaskChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentTaskChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentTaskChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentTaskChild: TypeAlias = Annotated[
    Union[
        DocumentTaskChildBlob,
        DocumentTaskChildCallout,
        DocumentTaskChildChunk,
        DocumentTaskChildCode,
        DocumentTaskChildComment,
        DocumentTaskChildDivider,
        DocumentTaskChildEquation,
        DocumentTaskChildFootnote,
        DocumentTaskChildHeading,
        DocumentTaskChildImage,
        DocumentTaskChildLink,
        DocumentTaskChildLineBreak,
        DocumentTaskChildList,
        DocumentTaskChildListItem,
        DocumentTaskChildParagraph,
        DocumentTaskChildQuote,
        DocumentTaskChildTable,
        DocumentTaskChildTableCell,
        DocumentTaskChildTableRow,
        DocumentTaskChildText,
        DocumentTaskChildToDo,
        DocumentTaskChildToolCall,
        DocumentTaskChildToolResult,
        DocumentTaskChildTraceMessage,
        DocumentTaskChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentTaskCommentSenderChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentSenderChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentSenderChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentSenderChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentSenderChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentSenderChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentSenderChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentSenderChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentSenderChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentSenderChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentSenderChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentSenderChild: TypeAlias = Union[
    DocumentTaskCommentSenderChildBlob,
    DocumentTaskCommentSenderChildCode,
    DocumentTaskCommentSenderChildComment,
    DocumentTaskCommentSenderChildDivider,
    DocumentTaskCommentSenderChildImage,
    DocumentTaskCommentSenderChildLink,
    DocumentTaskCommentSenderChildLineBreak,
    DocumentTaskCommentSenderChildText,
    DocumentTaskCommentSenderChildToolCall,
    DocumentTaskCommentSenderChildToolResult,
    DocumentTaskCommentSenderChildTraceMessage,
    object,
]


class DocumentTaskCommentSender(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[List[str]] = None

    children: Optional[List[DocumentTaskCommentSenderChild]] = None

    company: Optional[str] = None

    company_ids: Optional[List[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[List[str]] = None

    email: Optional[str] = None

    emails: Optional[List[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


class DocumentTaskCommentChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildCalloutChild: TypeAlias = Union[
    DocumentTaskCommentChildCalloutChildBlob,
    DocumentTaskCommentChildCalloutChildCode,
    DocumentTaskCommentChildCalloutChildComment,
    DocumentTaskCommentChildCalloutChildDivider,
    DocumentTaskCommentChildCalloutChildImage,
    DocumentTaskCommentChildCalloutChildLink,
    DocumentTaskCommentChildCalloutChildLineBreak,
    DocumentTaskCommentChildCalloutChildText,
    DocumentTaskCommentChildCalloutChildToolCall,
    DocumentTaskCommentChildCalloutChildToolResult,
    DocumentTaskCommentChildCalloutChildTraceMessage,
    object,
]


class DocumentTaskCommentChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskCommentChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentTaskCommentChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildChunkChild: TypeAlias = Union[
    DocumentTaskCommentChildChunkChildBlob,
    DocumentTaskCommentChildChunkChildCode,
    DocumentTaskCommentChildChunkChildComment,
    DocumentTaskCommentChildChunkChildDivider,
    DocumentTaskCommentChildChunkChildImage,
    DocumentTaskCommentChildChunkChildLink,
    DocumentTaskCommentChildChunkChildLineBreak,
    DocumentTaskCommentChildChunkChildText,
    DocumentTaskCommentChildChunkChildToolCall,
    DocumentTaskCommentChildChunkChildToolResult,
    DocumentTaskCommentChildChunkChildTraceMessage,
    object,
]


class DocumentTaskCommentChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskCommentChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentTaskCommentChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildEquationChild: TypeAlias = Union[
    DocumentTaskCommentChildEquationChildBlob,
    DocumentTaskCommentChildEquationChildCode,
    DocumentTaskCommentChildEquationChildComment,
    DocumentTaskCommentChildEquationChildDivider,
    DocumentTaskCommentChildEquationChildImage,
    DocumentTaskCommentChildEquationChildLink,
    DocumentTaskCommentChildEquationChildLineBreak,
    DocumentTaskCommentChildEquationChildText,
    DocumentTaskCommentChildEquationChildToolCall,
    DocumentTaskCommentChildEquationChildToolResult,
    DocumentTaskCommentChildEquationChildTraceMessage,
    object,
]


class DocumentTaskCommentChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskCommentChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentTaskCommentChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildFootnoteChild: TypeAlias = Union[
    DocumentTaskCommentChildFootnoteChildBlob,
    DocumentTaskCommentChildFootnoteChildCode,
    DocumentTaskCommentChildFootnoteChildComment,
    DocumentTaskCommentChildFootnoteChildDivider,
    DocumentTaskCommentChildFootnoteChildImage,
    DocumentTaskCommentChildFootnoteChildLink,
    DocumentTaskCommentChildFootnoteChildLineBreak,
    DocumentTaskCommentChildFootnoteChildText,
    DocumentTaskCommentChildFootnoteChildToolCall,
    DocumentTaskCommentChildFootnoteChildToolResult,
    DocumentTaskCommentChildFootnoteChildTraceMessage,
    object,
]


class DocumentTaskCommentChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskCommentChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentTaskCommentChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildHeadingChild: TypeAlias = Union[
    DocumentTaskCommentChildHeadingChildBlob,
    DocumentTaskCommentChildHeadingChildCode,
    DocumentTaskCommentChildHeadingChildComment,
    DocumentTaskCommentChildHeadingChildDivider,
    DocumentTaskCommentChildHeadingChildImage,
    DocumentTaskCommentChildHeadingChildLink,
    DocumentTaskCommentChildHeadingChildLineBreak,
    DocumentTaskCommentChildHeadingChildText,
    DocumentTaskCommentChildHeadingChildToolCall,
    DocumentTaskCommentChildHeadingChildToolResult,
    DocumentTaskCommentChildHeadingChildTraceMessage,
    object,
]


class DocumentTaskCommentChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentTaskCommentChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentTaskCommentChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentTaskCommentChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildListItemChild: TypeAlias = Union[
    DocumentTaskCommentChildListItemChildBlob,
    DocumentTaskCommentChildListItemChildCode,
    DocumentTaskCommentChildListItemChildComment,
    DocumentTaskCommentChildListItemChildDivider,
    DocumentTaskCommentChildListItemChildImage,
    DocumentTaskCommentChildListItemChildLink,
    DocumentTaskCommentChildListItemChildLineBreak,
    DocumentTaskCommentChildListItemChildText,
    DocumentTaskCommentChildListItemChildToolCall,
    DocumentTaskCommentChildListItemChildToolResult,
    DocumentTaskCommentChildListItemChildTraceMessage,
    object,
]


class DocumentTaskCommentChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskCommentChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentTaskCommentChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildParagraphChild: TypeAlias = Union[
    DocumentTaskCommentChildParagraphChildBlob,
    DocumentTaskCommentChildParagraphChildCode,
    DocumentTaskCommentChildParagraphChildComment,
    DocumentTaskCommentChildParagraphChildDivider,
    DocumentTaskCommentChildParagraphChildImage,
    DocumentTaskCommentChildParagraphChildLink,
    DocumentTaskCommentChildParagraphChildLineBreak,
    DocumentTaskCommentChildParagraphChildText,
    DocumentTaskCommentChildParagraphChildToolCall,
    DocumentTaskCommentChildParagraphChildToolResult,
    DocumentTaskCommentChildParagraphChildTraceMessage,
    object,
]


class DocumentTaskCommentChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskCommentChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentTaskCommentChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildQuoteChild: TypeAlias = Union[
    DocumentTaskCommentChildQuoteChildBlob,
    DocumentTaskCommentChildQuoteChildCode,
    DocumentTaskCommentChildQuoteChildComment,
    DocumentTaskCommentChildQuoteChildDivider,
    DocumentTaskCommentChildQuoteChildImage,
    DocumentTaskCommentChildQuoteChildLink,
    DocumentTaskCommentChildQuoteChildLineBreak,
    DocumentTaskCommentChildQuoteChildText,
    DocumentTaskCommentChildQuoteChildToolCall,
    DocumentTaskCommentChildQuoteChildToolResult,
    DocumentTaskCommentChildQuoteChildTraceMessage,
    object,
]


class DocumentTaskCommentChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskCommentChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentTaskCommentChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentTaskCommentChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildTableCellChild: TypeAlias = Union[
    DocumentTaskCommentChildTableCellChildBlob,
    DocumentTaskCommentChildTableCellChildCode,
    DocumentTaskCommentChildTableCellChildComment,
    DocumentTaskCommentChildTableCellChildDivider,
    DocumentTaskCommentChildTableCellChildImage,
    DocumentTaskCommentChildTableCellChildLink,
    DocumentTaskCommentChildTableCellChildLineBreak,
    DocumentTaskCommentChildTableCellChildText,
    DocumentTaskCommentChildTableCellChildToolCall,
    DocumentTaskCommentChildTableCellChildToolResult,
    DocumentTaskCommentChildTableCellChildTraceMessage,
    object,
]


class DocumentTaskCommentChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentTaskCommentChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentTaskCommentChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentTaskCommentChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentChildToDoChild: TypeAlias = Union[
    DocumentTaskCommentChildToDoChildBlob,
    DocumentTaskCommentChildToDoChildCode,
    DocumentTaskCommentChildToDoChildComment,
    DocumentTaskCommentChildToDoChildDivider,
    DocumentTaskCommentChildToDoChildImage,
    DocumentTaskCommentChildToDoChildLink,
    DocumentTaskCommentChildToDoChildLineBreak,
    DocumentTaskCommentChildToDoChildText,
    DocumentTaskCommentChildToDoChildToolCall,
    DocumentTaskCommentChildToDoChildToolResult,
    DocumentTaskCommentChildToDoChildTraceMessage,
    object,
]


class DocumentTaskCommentChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentTaskCommentChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentTaskCommentChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentTaskCommentChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentTaskCommentChild: TypeAlias = Annotated[
    Union[
        DocumentTaskCommentChildBlob,
        DocumentTaskCommentChildCallout,
        DocumentTaskCommentChildChunk,
        DocumentTaskCommentChildCode,
        DocumentTaskCommentChildComment,
        DocumentTaskCommentChildDivider,
        DocumentTaskCommentChildEquation,
        DocumentTaskCommentChildFootnote,
        DocumentTaskCommentChildHeading,
        DocumentTaskCommentChildImage,
        DocumentTaskCommentChildLink,
        DocumentTaskCommentChildLineBreak,
        DocumentTaskCommentChildList,
        DocumentTaskCommentChildListItem,
        DocumentTaskCommentChildParagraph,
        DocumentTaskCommentChildQuote,
        DocumentTaskCommentChildTable,
        DocumentTaskCommentChildTableCell,
        DocumentTaskCommentChildTableRow,
        DocumentTaskCommentChildText,
        DocumentTaskCommentChildToDo,
        DocumentTaskCommentChildToolCall,
        DocumentTaskCommentChildToolResult,
        DocumentTaskCommentChildTraceMessage,
        DocumentTaskCommentChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentTaskCommentMentionedUserChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTaskCommentMentionedUserChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTaskCommentMentionedUserChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTaskCommentMentionedUserChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTaskCommentMentionedUserChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTaskCommentMentionedUserChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTaskCommentMentionedUserChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTaskCommentMentionedUserChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTaskCommentMentionedUserChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTaskCommentMentionedUserChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTaskCommentMentionedUserChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTaskCommentMentionedUserChild: TypeAlias = Union[
    DocumentTaskCommentMentionedUserChildBlob,
    DocumentTaskCommentMentionedUserChildCode,
    DocumentTaskCommentMentionedUserChildComment,
    DocumentTaskCommentMentionedUserChildDivider,
    DocumentTaskCommentMentionedUserChildImage,
    DocumentTaskCommentMentionedUserChildLink,
    DocumentTaskCommentMentionedUserChildLineBreak,
    DocumentTaskCommentMentionedUserChildText,
    DocumentTaskCommentMentionedUserChildToolCall,
    DocumentTaskCommentMentionedUserChildToolResult,
    DocumentTaskCommentMentionedUserChildTraceMessage,
    object,
]


class DocumentTaskCommentMentionedUser(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[List[str]] = None

    children: Optional[List[DocumentTaskCommentMentionedUserChild]] = None

    company: Optional[str] = None

    company_ids: Optional[List[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[List[str]] = None

    email: Optional[str] = None

    emails: Optional[List[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


class DocumentTaskComment(BaseModel):
    date: datetime

    sender: DocumentTaskCommentSender

    id: Optional[str] = None

    channel: Optional[str] = None
    """
    The channel or platform where the message was posted, if this Message is not
    explicitly part of a conversation
    """

    children: Optional[List[DocumentTaskCommentChild]] = None

    external_id: Optional[str] = None
    """Provider message id (e.g. Slack ts, Gmail message id) — merge-dedup key"""

    is_self: Optional[bool] = None

    mentioned_users: Optional[List[DocumentTaskCommentMentionedUser]] = None

    num_replies: Optional[int] = None

    replies: Optional[List[object]] = None
    """The replies or comments to the message"""

    text: Optional[str] = None

    thread_id: Optional[str] = None

    title: Optional[str] = None
    """The subject or title of the message"""

    type: Optional[Literal["message"]] = None

    updated_at: Optional[datetime] = None

    upvotes: Optional[int] = None
    """The number of upvotes, likes, or reactions on the message"""


class DocumentTask(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentTaskChild]] = None

    comments: Optional[List[DocumentTaskComment]] = None

    due_at: Optional[datetime] = None

    priority: Optional[Literal["urgent", "high", "medium", "low"]] = None

    status: Optional[Literal["completed", "not_started", "in_progress", "cancelled"]] = None

    text: Optional[str] = None

    type: Optional[Literal["task"]] = None


class DocumentPersonChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentPersonChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentPersonChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentPersonChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentPersonChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentPersonChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentPersonChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentPersonChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentPersonChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentPersonChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentPersonChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentPersonChild: TypeAlias = Union[
    DocumentPersonChildBlob,
    DocumentPersonChildCode,
    DocumentPersonChildComment,
    DocumentPersonChildDivider,
    DocumentPersonChildImage,
    DocumentPersonChildLink,
    DocumentPersonChildLineBreak,
    DocumentPersonChildText,
    DocumentPersonChildToolCall,
    DocumentPersonChildToolResult,
    DocumentPersonChildTraceMessage,
    object,
]


class DocumentPerson(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[List[str]] = None

    children: Optional[List[DocumentPersonChild]] = None

    company: Optional[str] = None

    company_ids: Optional[List[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[List[str]] = None

    email: Optional[str] = None

    emails: Optional[List[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


class DocumentMessageSenderChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageSenderChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageSenderChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageSenderChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageSenderChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageSenderChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageSenderChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageSenderChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageSenderChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageSenderChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageSenderChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageSenderChild: TypeAlias = Union[
    DocumentMessageSenderChildBlob,
    DocumentMessageSenderChildCode,
    DocumentMessageSenderChildComment,
    DocumentMessageSenderChildDivider,
    DocumentMessageSenderChildImage,
    DocumentMessageSenderChildLink,
    DocumentMessageSenderChildLineBreak,
    DocumentMessageSenderChildText,
    DocumentMessageSenderChildToolCall,
    DocumentMessageSenderChildToolResult,
    DocumentMessageSenderChildTraceMessage,
    object,
]


class DocumentMessageSender(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[List[str]] = None

    children: Optional[List[DocumentMessageSenderChild]] = None

    company: Optional[str] = None

    company_ids: Optional[List[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[List[str]] = None

    email: Optional[str] = None

    emails: Optional[List[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


class DocumentMessageChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildCalloutChild: TypeAlias = Union[
    DocumentMessageChildCalloutChildBlob,
    DocumentMessageChildCalloutChildCode,
    DocumentMessageChildCalloutChildComment,
    DocumentMessageChildCalloutChildDivider,
    DocumentMessageChildCalloutChildImage,
    DocumentMessageChildCalloutChildLink,
    DocumentMessageChildCalloutChildLineBreak,
    DocumentMessageChildCalloutChildText,
    DocumentMessageChildCalloutChildToolCall,
    DocumentMessageChildCalloutChildToolResult,
    DocumentMessageChildCalloutChildTraceMessage,
    object,
]


class DocumentMessageChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentMessageChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentMessageChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildChunkChild: TypeAlias = Union[
    DocumentMessageChildChunkChildBlob,
    DocumentMessageChildChunkChildCode,
    DocumentMessageChildChunkChildComment,
    DocumentMessageChildChunkChildDivider,
    DocumentMessageChildChunkChildImage,
    DocumentMessageChildChunkChildLink,
    DocumentMessageChildChunkChildLineBreak,
    DocumentMessageChildChunkChildText,
    DocumentMessageChildChunkChildToolCall,
    DocumentMessageChildChunkChildToolResult,
    DocumentMessageChildChunkChildTraceMessage,
    object,
]


class DocumentMessageChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentMessageChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentMessageChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildEquationChild: TypeAlias = Union[
    DocumentMessageChildEquationChildBlob,
    DocumentMessageChildEquationChildCode,
    DocumentMessageChildEquationChildComment,
    DocumentMessageChildEquationChildDivider,
    DocumentMessageChildEquationChildImage,
    DocumentMessageChildEquationChildLink,
    DocumentMessageChildEquationChildLineBreak,
    DocumentMessageChildEquationChildText,
    DocumentMessageChildEquationChildToolCall,
    DocumentMessageChildEquationChildToolResult,
    DocumentMessageChildEquationChildTraceMessage,
    object,
]


class DocumentMessageChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentMessageChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentMessageChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildFootnoteChild: TypeAlias = Union[
    DocumentMessageChildFootnoteChildBlob,
    DocumentMessageChildFootnoteChildCode,
    DocumentMessageChildFootnoteChildComment,
    DocumentMessageChildFootnoteChildDivider,
    DocumentMessageChildFootnoteChildImage,
    DocumentMessageChildFootnoteChildLink,
    DocumentMessageChildFootnoteChildLineBreak,
    DocumentMessageChildFootnoteChildText,
    DocumentMessageChildFootnoteChildToolCall,
    DocumentMessageChildFootnoteChildToolResult,
    DocumentMessageChildFootnoteChildTraceMessage,
    object,
]


class DocumentMessageChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentMessageChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentMessageChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildHeadingChild: TypeAlias = Union[
    DocumentMessageChildHeadingChildBlob,
    DocumentMessageChildHeadingChildCode,
    DocumentMessageChildHeadingChildComment,
    DocumentMessageChildHeadingChildDivider,
    DocumentMessageChildHeadingChildImage,
    DocumentMessageChildHeadingChildLink,
    DocumentMessageChildHeadingChildLineBreak,
    DocumentMessageChildHeadingChildText,
    DocumentMessageChildHeadingChildToolCall,
    DocumentMessageChildHeadingChildToolResult,
    DocumentMessageChildHeadingChildTraceMessage,
    object,
]


class DocumentMessageChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentMessageChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentMessageChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentMessageChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildListItemChild: TypeAlias = Union[
    DocumentMessageChildListItemChildBlob,
    DocumentMessageChildListItemChildCode,
    DocumentMessageChildListItemChildComment,
    DocumentMessageChildListItemChildDivider,
    DocumentMessageChildListItemChildImage,
    DocumentMessageChildListItemChildLink,
    DocumentMessageChildListItemChildLineBreak,
    DocumentMessageChildListItemChildText,
    DocumentMessageChildListItemChildToolCall,
    DocumentMessageChildListItemChildToolResult,
    DocumentMessageChildListItemChildTraceMessage,
    object,
]


class DocumentMessageChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentMessageChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentMessageChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildParagraphChild: TypeAlias = Union[
    DocumentMessageChildParagraphChildBlob,
    DocumentMessageChildParagraphChildCode,
    DocumentMessageChildParagraphChildComment,
    DocumentMessageChildParagraphChildDivider,
    DocumentMessageChildParagraphChildImage,
    DocumentMessageChildParagraphChildLink,
    DocumentMessageChildParagraphChildLineBreak,
    DocumentMessageChildParagraphChildText,
    DocumentMessageChildParagraphChildToolCall,
    DocumentMessageChildParagraphChildToolResult,
    DocumentMessageChildParagraphChildTraceMessage,
    object,
]


class DocumentMessageChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentMessageChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentMessageChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildQuoteChild: TypeAlias = Union[
    DocumentMessageChildQuoteChildBlob,
    DocumentMessageChildQuoteChildCode,
    DocumentMessageChildQuoteChildComment,
    DocumentMessageChildQuoteChildDivider,
    DocumentMessageChildQuoteChildImage,
    DocumentMessageChildQuoteChildLink,
    DocumentMessageChildQuoteChildLineBreak,
    DocumentMessageChildQuoteChildText,
    DocumentMessageChildQuoteChildToolCall,
    DocumentMessageChildQuoteChildToolResult,
    DocumentMessageChildQuoteChildTraceMessage,
    object,
]


class DocumentMessageChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentMessageChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentMessageChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentMessageChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildTableCellChild: TypeAlias = Union[
    DocumentMessageChildTableCellChildBlob,
    DocumentMessageChildTableCellChildCode,
    DocumentMessageChildTableCellChildComment,
    DocumentMessageChildTableCellChildDivider,
    DocumentMessageChildTableCellChildImage,
    DocumentMessageChildTableCellChildLink,
    DocumentMessageChildTableCellChildLineBreak,
    DocumentMessageChildTableCellChildText,
    DocumentMessageChildTableCellChildToolCall,
    DocumentMessageChildTableCellChildToolResult,
    DocumentMessageChildTableCellChildTraceMessage,
    object,
]


class DocumentMessageChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentMessageChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentMessageChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentMessageChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageChildToDoChild: TypeAlias = Union[
    DocumentMessageChildToDoChildBlob,
    DocumentMessageChildToDoChildCode,
    DocumentMessageChildToDoChildComment,
    DocumentMessageChildToDoChildDivider,
    DocumentMessageChildToDoChildImage,
    DocumentMessageChildToDoChildLink,
    DocumentMessageChildToDoChildLineBreak,
    DocumentMessageChildToDoChildText,
    DocumentMessageChildToDoChildToolCall,
    DocumentMessageChildToDoChildToolResult,
    DocumentMessageChildToDoChildTraceMessage,
    object,
]


class DocumentMessageChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentMessageChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentMessageChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentMessageChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentMessageChild: TypeAlias = Annotated[
    Union[
        DocumentMessageChildBlob,
        DocumentMessageChildCallout,
        DocumentMessageChildChunk,
        DocumentMessageChildCode,
        DocumentMessageChildComment,
        DocumentMessageChildDivider,
        DocumentMessageChildEquation,
        DocumentMessageChildFootnote,
        DocumentMessageChildHeading,
        DocumentMessageChildImage,
        DocumentMessageChildLink,
        DocumentMessageChildLineBreak,
        DocumentMessageChildList,
        DocumentMessageChildListItem,
        DocumentMessageChildParagraph,
        DocumentMessageChildQuote,
        DocumentMessageChildTable,
        DocumentMessageChildTableCell,
        DocumentMessageChildTableRow,
        DocumentMessageChildText,
        DocumentMessageChildToDo,
        DocumentMessageChildToolCall,
        DocumentMessageChildToolResult,
        DocumentMessageChildTraceMessage,
        DocumentMessageChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentMessageMentionedUserChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentMessageMentionedUserChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentMessageMentionedUserChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentMessageMentionedUserChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentMessageMentionedUserChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentMessageMentionedUserChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentMessageMentionedUserChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentMessageMentionedUserChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentMessageMentionedUserChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentMessageMentionedUserChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentMessageMentionedUserChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentMessageMentionedUserChild: TypeAlias = Union[
    DocumentMessageMentionedUserChildBlob,
    DocumentMessageMentionedUserChildCode,
    DocumentMessageMentionedUserChildComment,
    DocumentMessageMentionedUserChildDivider,
    DocumentMessageMentionedUserChildImage,
    DocumentMessageMentionedUserChildLink,
    DocumentMessageMentionedUserChildLineBreak,
    DocumentMessageMentionedUserChildText,
    DocumentMessageMentionedUserChildToolCall,
    DocumentMessageMentionedUserChildToolResult,
    DocumentMessageMentionedUserChildTraceMessage,
    object,
]


class DocumentMessageMentionedUser(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[List[str]] = None

    children: Optional[List[DocumentMessageMentionedUserChild]] = None

    company: Optional[str] = None

    company_ids: Optional[List[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[List[str]] = None

    email: Optional[str] = None

    emails: Optional[List[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


class DocumentMessage(BaseModel):
    date: datetime

    sender: DocumentMessageSender

    id: Optional[str] = None

    channel: Optional[str] = None
    """
    The channel or platform where the message was posted, if this Message is not
    explicitly part of a conversation
    """

    children: Optional[List[DocumentMessageChild]] = None

    external_id: Optional[str] = None
    """Provider message id (e.g. Slack ts, Gmail message id) — merge-dedup key"""

    is_self: Optional[bool] = None

    mentioned_users: Optional[List[DocumentMessageMentionedUser]] = None

    num_replies: Optional[int] = None

    replies: Optional[List[object]] = None
    """The replies or comments to the message"""

    text: Optional[str] = None

    thread_id: Optional[str] = None

    title: Optional[str] = None
    """The subject or title of the message"""

    type: Optional[Literal["message"]] = None

    updated_at: Optional[datetime] = None

    upvotes: Optional[int] = None
    """The number of upvotes, likes, or reactions on the message"""


class DocumentEventAttendeeChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventAttendeeChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventAttendeeChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventAttendeeChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventAttendeeChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventAttendeeChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventAttendeeChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventAttendeeChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventAttendeeChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventAttendeeChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventAttendeeChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventAttendeeChild: TypeAlias = Union[
    DocumentEventAttendeeChildBlob,
    DocumentEventAttendeeChildCode,
    DocumentEventAttendeeChildComment,
    DocumentEventAttendeeChildDivider,
    DocumentEventAttendeeChildImage,
    DocumentEventAttendeeChildLink,
    DocumentEventAttendeeChildLineBreak,
    DocumentEventAttendeeChildText,
    DocumentEventAttendeeChildToolCall,
    DocumentEventAttendeeChildToolResult,
    DocumentEventAttendeeChildTraceMessage,
    object,
]


class DocumentEventAttendee(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[List[str]] = None

    children: Optional[List[DocumentEventAttendeeChild]] = None

    company: Optional[str] = None

    company_ids: Optional[List[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[List[str]] = None

    email: Optional[str] = None

    emails: Optional[List[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


class DocumentEventChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildCalloutChild: TypeAlias = Union[
    DocumentEventChildCalloutChildBlob,
    DocumentEventChildCalloutChildCode,
    DocumentEventChildCalloutChildComment,
    DocumentEventChildCalloutChildDivider,
    DocumentEventChildCalloutChildImage,
    DocumentEventChildCalloutChildLink,
    DocumentEventChildCalloutChildLineBreak,
    DocumentEventChildCalloutChildText,
    DocumentEventChildCalloutChildToolCall,
    DocumentEventChildCalloutChildToolResult,
    DocumentEventChildCalloutChildTraceMessage,
    object,
]


class DocumentEventChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentEventChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentEventChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildChunkChild: TypeAlias = Union[
    DocumentEventChildChunkChildBlob,
    DocumentEventChildChunkChildCode,
    DocumentEventChildChunkChildComment,
    DocumentEventChildChunkChildDivider,
    DocumentEventChildChunkChildImage,
    DocumentEventChildChunkChildLink,
    DocumentEventChildChunkChildLineBreak,
    DocumentEventChildChunkChildText,
    DocumentEventChildChunkChildToolCall,
    DocumentEventChildChunkChildToolResult,
    DocumentEventChildChunkChildTraceMessage,
    object,
]


class DocumentEventChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentEventChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentEventChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildEquationChild: TypeAlias = Union[
    DocumentEventChildEquationChildBlob,
    DocumentEventChildEquationChildCode,
    DocumentEventChildEquationChildComment,
    DocumentEventChildEquationChildDivider,
    DocumentEventChildEquationChildImage,
    DocumentEventChildEquationChildLink,
    DocumentEventChildEquationChildLineBreak,
    DocumentEventChildEquationChildText,
    DocumentEventChildEquationChildToolCall,
    DocumentEventChildEquationChildToolResult,
    DocumentEventChildEquationChildTraceMessage,
    object,
]


class DocumentEventChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentEventChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentEventChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildFootnoteChild: TypeAlias = Union[
    DocumentEventChildFootnoteChildBlob,
    DocumentEventChildFootnoteChildCode,
    DocumentEventChildFootnoteChildComment,
    DocumentEventChildFootnoteChildDivider,
    DocumentEventChildFootnoteChildImage,
    DocumentEventChildFootnoteChildLink,
    DocumentEventChildFootnoteChildLineBreak,
    DocumentEventChildFootnoteChildText,
    DocumentEventChildFootnoteChildToolCall,
    DocumentEventChildFootnoteChildToolResult,
    DocumentEventChildFootnoteChildTraceMessage,
    object,
]


class DocumentEventChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentEventChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentEventChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildHeadingChild: TypeAlias = Union[
    DocumentEventChildHeadingChildBlob,
    DocumentEventChildHeadingChildCode,
    DocumentEventChildHeadingChildComment,
    DocumentEventChildHeadingChildDivider,
    DocumentEventChildHeadingChildImage,
    DocumentEventChildHeadingChildLink,
    DocumentEventChildHeadingChildLineBreak,
    DocumentEventChildHeadingChildText,
    DocumentEventChildHeadingChildToolCall,
    DocumentEventChildHeadingChildToolResult,
    DocumentEventChildHeadingChildTraceMessage,
    object,
]


class DocumentEventChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentEventChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentEventChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentEventChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildListItemChild: TypeAlias = Union[
    DocumentEventChildListItemChildBlob,
    DocumentEventChildListItemChildCode,
    DocumentEventChildListItemChildComment,
    DocumentEventChildListItemChildDivider,
    DocumentEventChildListItemChildImage,
    DocumentEventChildListItemChildLink,
    DocumentEventChildListItemChildLineBreak,
    DocumentEventChildListItemChildText,
    DocumentEventChildListItemChildToolCall,
    DocumentEventChildListItemChildToolResult,
    DocumentEventChildListItemChildTraceMessage,
    object,
]


class DocumentEventChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentEventChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentEventChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildParagraphChild: TypeAlias = Union[
    DocumentEventChildParagraphChildBlob,
    DocumentEventChildParagraphChildCode,
    DocumentEventChildParagraphChildComment,
    DocumentEventChildParagraphChildDivider,
    DocumentEventChildParagraphChildImage,
    DocumentEventChildParagraphChildLink,
    DocumentEventChildParagraphChildLineBreak,
    DocumentEventChildParagraphChildText,
    DocumentEventChildParagraphChildToolCall,
    DocumentEventChildParagraphChildToolResult,
    DocumentEventChildParagraphChildTraceMessage,
    object,
]


class DocumentEventChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentEventChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentEventChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildQuoteChild: TypeAlias = Union[
    DocumentEventChildQuoteChildBlob,
    DocumentEventChildQuoteChildCode,
    DocumentEventChildQuoteChildComment,
    DocumentEventChildQuoteChildDivider,
    DocumentEventChildQuoteChildImage,
    DocumentEventChildQuoteChildLink,
    DocumentEventChildQuoteChildLineBreak,
    DocumentEventChildQuoteChildText,
    DocumentEventChildQuoteChildToolCall,
    DocumentEventChildQuoteChildToolResult,
    DocumentEventChildQuoteChildTraceMessage,
    object,
]


class DocumentEventChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentEventChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentEventChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentEventChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildTableCellChild: TypeAlias = Union[
    DocumentEventChildTableCellChildBlob,
    DocumentEventChildTableCellChildCode,
    DocumentEventChildTableCellChildComment,
    DocumentEventChildTableCellChildDivider,
    DocumentEventChildTableCellChildImage,
    DocumentEventChildTableCellChildLink,
    DocumentEventChildTableCellChildLineBreak,
    DocumentEventChildTableCellChildText,
    DocumentEventChildTableCellChildToolCall,
    DocumentEventChildTableCellChildToolResult,
    DocumentEventChildTableCellChildTraceMessage,
    object,
]


class DocumentEventChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentEventChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentEventChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentEventChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentEventChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentEventChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentEventChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentEventChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentEventChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentEventChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentEventChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentEventChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentEventChildToDoChild: TypeAlias = Union[
    DocumentEventChildToDoChildBlob,
    DocumentEventChildToDoChildCode,
    DocumentEventChildToDoChildComment,
    DocumentEventChildToDoChildDivider,
    DocumentEventChildToDoChildImage,
    DocumentEventChildToDoChildLink,
    DocumentEventChildToDoChildLineBreak,
    DocumentEventChildToDoChildText,
    DocumentEventChildToDoChildToolCall,
    DocumentEventChildToDoChildToolResult,
    DocumentEventChildToDoChildTraceMessage,
    object,
]


class DocumentEventChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentEventChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentEventChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentEventChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentEventChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentEventChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentEventChild: TypeAlias = Annotated[
    Union[
        DocumentEventChildBlob,
        DocumentEventChildCallout,
        DocumentEventChildChunk,
        DocumentEventChildCode,
        DocumentEventChildComment,
        DocumentEventChildDivider,
        DocumentEventChildEquation,
        DocumentEventChildFootnote,
        DocumentEventChildHeading,
        DocumentEventChildImage,
        DocumentEventChildLink,
        DocumentEventChildLineBreak,
        DocumentEventChildList,
        DocumentEventChildListItem,
        DocumentEventChildParagraph,
        DocumentEventChildQuote,
        DocumentEventChildTable,
        DocumentEventChildTableCell,
        DocumentEventChildTableRow,
        DocumentEventChildText,
        DocumentEventChildToDo,
        DocumentEventChildToolCall,
        DocumentEventChildToolResult,
        DocumentEventChildTraceMessage,
        DocumentEventChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentEvent(BaseModel):
    id: Optional[str] = None

    attendees: Optional[List[DocumentEventAttendee]] = None

    children: Optional[List[DocumentEventChild]] = None

    end_at: Optional[datetime] = None

    location: Optional[str] = None

    meeting_url: Optional[str] = None

    start_at: Optional[datetime] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["event"]] = None


class DocumentFileChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildCalloutChild: TypeAlias = Union[
    DocumentFileChildCalloutChildBlob,
    DocumentFileChildCalloutChildCode,
    DocumentFileChildCalloutChildComment,
    DocumentFileChildCalloutChildDivider,
    DocumentFileChildCalloutChildImage,
    DocumentFileChildCalloutChildLink,
    DocumentFileChildCalloutChildLineBreak,
    DocumentFileChildCalloutChildText,
    DocumentFileChildCalloutChildToolCall,
    DocumentFileChildCalloutChildToolResult,
    DocumentFileChildCalloutChildTraceMessage,
    object,
]


class DocumentFileChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentFileChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentFileChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildChunkChild: TypeAlias = Union[
    DocumentFileChildChunkChildBlob,
    DocumentFileChildChunkChildCode,
    DocumentFileChildChunkChildComment,
    DocumentFileChildChunkChildDivider,
    DocumentFileChildChunkChildImage,
    DocumentFileChildChunkChildLink,
    DocumentFileChildChunkChildLineBreak,
    DocumentFileChildChunkChildText,
    DocumentFileChildChunkChildToolCall,
    DocumentFileChildChunkChildToolResult,
    DocumentFileChildChunkChildTraceMessage,
    object,
]


class DocumentFileChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentFileChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentFileChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildEquationChild: TypeAlias = Union[
    DocumentFileChildEquationChildBlob,
    DocumentFileChildEquationChildCode,
    DocumentFileChildEquationChildComment,
    DocumentFileChildEquationChildDivider,
    DocumentFileChildEquationChildImage,
    DocumentFileChildEquationChildLink,
    DocumentFileChildEquationChildLineBreak,
    DocumentFileChildEquationChildText,
    DocumentFileChildEquationChildToolCall,
    DocumentFileChildEquationChildToolResult,
    DocumentFileChildEquationChildTraceMessage,
    object,
]


class DocumentFileChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentFileChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentFileChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildFootnoteChild: TypeAlias = Union[
    DocumentFileChildFootnoteChildBlob,
    DocumentFileChildFootnoteChildCode,
    DocumentFileChildFootnoteChildComment,
    DocumentFileChildFootnoteChildDivider,
    DocumentFileChildFootnoteChildImage,
    DocumentFileChildFootnoteChildLink,
    DocumentFileChildFootnoteChildLineBreak,
    DocumentFileChildFootnoteChildText,
    DocumentFileChildFootnoteChildToolCall,
    DocumentFileChildFootnoteChildToolResult,
    DocumentFileChildFootnoteChildTraceMessage,
    object,
]


class DocumentFileChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentFileChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentFileChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildHeadingChild: TypeAlias = Union[
    DocumentFileChildHeadingChildBlob,
    DocumentFileChildHeadingChildCode,
    DocumentFileChildHeadingChildComment,
    DocumentFileChildHeadingChildDivider,
    DocumentFileChildHeadingChildImage,
    DocumentFileChildHeadingChildLink,
    DocumentFileChildHeadingChildLineBreak,
    DocumentFileChildHeadingChildText,
    DocumentFileChildHeadingChildToolCall,
    DocumentFileChildHeadingChildToolResult,
    DocumentFileChildHeadingChildTraceMessage,
    object,
]


class DocumentFileChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentFileChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentFileChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentFileChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildListItemChild: TypeAlias = Union[
    DocumentFileChildListItemChildBlob,
    DocumentFileChildListItemChildCode,
    DocumentFileChildListItemChildComment,
    DocumentFileChildListItemChildDivider,
    DocumentFileChildListItemChildImage,
    DocumentFileChildListItemChildLink,
    DocumentFileChildListItemChildLineBreak,
    DocumentFileChildListItemChildText,
    DocumentFileChildListItemChildToolCall,
    DocumentFileChildListItemChildToolResult,
    DocumentFileChildListItemChildTraceMessage,
    object,
]


class DocumentFileChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentFileChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentFileChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildParagraphChild: TypeAlias = Union[
    DocumentFileChildParagraphChildBlob,
    DocumentFileChildParagraphChildCode,
    DocumentFileChildParagraphChildComment,
    DocumentFileChildParagraphChildDivider,
    DocumentFileChildParagraphChildImage,
    DocumentFileChildParagraphChildLink,
    DocumentFileChildParagraphChildLineBreak,
    DocumentFileChildParagraphChildText,
    DocumentFileChildParagraphChildToolCall,
    DocumentFileChildParagraphChildToolResult,
    DocumentFileChildParagraphChildTraceMessage,
    object,
]


class DocumentFileChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentFileChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentFileChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildQuoteChild: TypeAlias = Union[
    DocumentFileChildQuoteChildBlob,
    DocumentFileChildQuoteChildCode,
    DocumentFileChildQuoteChildComment,
    DocumentFileChildQuoteChildDivider,
    DocumentFileChildQuoteChildImage,
    DocumentFileChildQuoteChildLink,
    DocumentFileChildQuoteChildLineBreak,
    DocumentFileChildQuoteChildText,
    DocumentFileChildQuoteChildToolCall,
    DocumentFileChildQuoteChildToolResult,
    DocumentFileChildQuoteChildTraceMessage,
    object,
]


class DocumentFileChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentFileChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentFileChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentFileChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildTableCellChild: TypeAlias = Union[
    DocumentFileChildTableCellChildBlob,
    DocumentFileChildTableCellChildCode,
    DocumentFileChildTableCellChildComment,
    DocumentFileChildTableCellChildDivider,
    DocumentFileChildTableCellChildImage,
    DocumentFileChildTableCellChildLink,
    DocumentFileChildTableCellChildLineBreak,
    DocumentFileChildTableCellChildText,
    DocumentFileChildTableCellChildToolCall,
    DocumentFileChildTableCellChildToolResult,
    DocumentFileChildTableCellChildTraceMessage,
    object,
]


class DocumentFileChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentFileChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentFileChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentFileChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentFileChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentFileChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentFileChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentFileChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentFileChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentFileChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentFileChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentFileChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentFileChildToDoChild: TypeAlias = Union[
    DocumentFileChildToDoChildBlob,
    DocumentFileChildToDoChildCode,
    DocumentFileChildToDoChildComment,
    DocumentFileChildToDoChildDivider,
    DocumentFileChildToDoChildImage,
    DocumentFileChildToDoChildLink,
    DocumentFileChildToDoChildLineBreak,
    DocumentFileChildToDoChildText,
    DocumentFileChildToDoChildToolCall,
    DocumentFileChildToDoChildToolResult,
    DocumentFileChildToDoChildTraceMessage,
    object,
]


class DocumentFileChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentFileChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentFileChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentFileChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentFileChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentFileChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentFileChild: TypeAlias = Annotated[
    Union[
        DocumentFileChildBlob,
        DocumentFileChildCallout,
        DocumentFileChildChunk,
        DocumentFileChildCode,
        DocumentFileChildComment,
        DocumentFileChildDivider,
        DocumentFileChildEquation,
        DocumentFileChildFootnote,
        DocumentFileChildHeading,
        DocumentFileChildImage,
        DocumentFileChildLink,
        DocumentFileChildLineBreak,
        DocumentFileChildList,
        DocumentFileChildListItem,
        DocumentFileChildParagraph,
        DocumentFileChildQuote,
        DocumentFileChildTable,
        DocumentFileChildTableCell,
        DocumentFileChildTableRow,
        DocumentFileChildText,
        DocumentFileChildToDo,
        DocumentFileChildToolCall,
        DocumentFileChildToolResult,
        DocumentFileChildTraceMessage,
        DocumentFileChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentFile(BaseModel):
    content_type: str

    filename: str

    id: Optional[str] = None

    children: Optional[List[DocumentFileChild]] = None

    path: Optional[List[str]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["file"]] = None


class DocumentConversationChildSenderChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildSenderChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildSenderChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildSenderChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildSenderChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildSenderChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildSenderChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildSenderChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildSenderChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildSenderChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildSenderChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildSenderChild: TypeAlias = Union[
    DocumentConversationChildSenderChildBlob,
    DocumentConversationChildSenderChildCode,
    DocumentConversationChildSenderChildComment,
    DocumentConversationChildSenderChildDivider,
    DocumentConversationChildSenderChildImage,
    DocumentConversationChildSenderChildLink,
    DocumentConversationChildSenderChildLineBreak,
    DocumentConversationChildSenderChildText,
    DocumentConversationChildSenderChildToolCall,
    DocumentConversationChildSenderChildToolResult,
    DocumentConversationChildSenderChildTraceMessage,
    object,
]


class DocumentConversationChildSender(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[List[str]] = None

    children: Optional[List[DocumentConversationChildSenderChild]] = None

    company: Optional[str] = None

    company_ids: Optional[List[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[List[str]] = None

    email: Optional[str] = None

    emails: Optional[List[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


class DocumentConversationChildChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildCalloutChild: TypeAlias = Union[
    DocumentConversationChildChildCalloutChildBlob,
    DocumentConversationChildChildCalloutChildCode,
    DocumentConversationChildChildCalloutChildComment,
    DocumentConversationChildChildCalloutChildDivider,
    DocumentConversationChildChildCalloutChildImage,
    DocumentConversationChildChildCalloutChildLink,
    DocumentConversationChildChildCalloutChildLineBreak,
    DocumentConversationChildChildCalloutChildText,
    DocumentConversationChildChildCalloutChildToolCall,
    DocumentConversationChildChildCalloutChildToolResult,
    DocumentConversationChildChildCalloutChildTraceMessage,
    object,
]


class DocumentConversationChildChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentConversationChildChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentConversationChildChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildChunkChild: TypeAlias = Union[
    DocumentConversationChildChildChunkChildBlob,
    DocumentConversationChildChildChunkChildCode,
    DocumentConversationChildChildChunkChildComment,
    DocumentConversationChildChildChunkChildDivider,
    DocumentConversationChildChildChunkChildImage,
    DocumentConversationChildChildChunkChildLink,
    DocumentConversationChildChildChunkChildLineBreak,
    DocumentConversationChildChildChunkChildText,
    DocumentConversationChildChildChunkChildToolCall,
    DocumentConversationChildChildChunkChildToolResult,
    DocumentConversationChildChildChunkChildTraceMessage,
    object,
]


class DocumentConversationChildChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentConversationChildChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentConversationChildChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildEquationChild: TypeAlias = Union[
    DocumentConversationChildChildEquationChildBlob,
    DocumentConversationChildChildEquationChildCode,
    DocumentConversationChildChildEquationChildComment,
    DocumentConversationChildChildEquationChildDivider,
    DocumentConversationChildChildEquationChildImage,
    DocumentConversationChildChildEquationChildLink,
    DocumentConversationChildChildEquationChildLineBreak,
    DocumentConversationChildChildEquationChildText,
    DocumentConversationChildChildEquationChildToolCall,
    DocumentConversationChildChildEquationChildToolResult,
    DocumentConversationChildChildEquationChildTraceMessage,
    object,
]


class DocumentConversationChildChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentConversationChildChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentConversationChildChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildFootnoteChild: TypeAlias = Union[
    DocumentConversationChildChildFootnoteChildBlob,
    DocumentConversationChildChildFootnoteChildCode,
    DocumentConversationChildChildFootnoteChildComment,
    DocumentConversationChildChildFootnoteChildDivider,
    DocumentConversationChildChildFootnoteChildImage,
    DocumentConversationChildChildFootnoteChildLink,
    DocumentConversationChildChildFootnoteChildLineBreak,
    DocumentConversationChildChildFootnoteChildText,
    DocumentConversationChildChildFootnoteChildToolCall,
    DocumentConversationChildChildFootnoteChildToolResult,
    DocumentConversationChildChildFootnoteChildTraceMessage,
    object,
]


class DocumentConversationChildChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentConversationChildChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentConversationChildChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildHeadingChild: TypeAlias = Union[
    DocumentConversationChildChildHeadingChildBlob,
    DocumentConversationChildChildHeadingChildCode,
    DocumentConversationChildChildHeadingChildComment,
    DocumentConversationChildChildHeadingChildDivider,
    DocumentConversationChildChildHeadingChildImage,
    DocumentConversationChildChildHeadingChildLink,
    DocumentConversationChildChildHeadingChildLineBreak,
    DocumentConversationChildChildHeadingChildText,
    DocumentConversationChildChildHeadingChildToolCall,
    DocumentConversationChildChildHeadingChildToolResult,
    DocumentConversationChildChildHeadingChildTraceMessage,
    object,
]


class DocumentConversationChildChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentConversationChildChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentConversationChildChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentConversationChildChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildListItemChild: TypeAlias = Union[
    DocumentConversationChildChildListItemChildBlob,
    DocumentConversationChildChildListItemChildCode,
    DocumentConversationChildChildListItemChildComment,
    DocumentConversationChildChildListItemChildDivider,
    DocumentConversationChildChildListItemChildImage,
    DocumentConversationChildChildListItemChildLink,
    DocumentConversationChildChildListItemChildLineBreak,
    DocumentConversationChildChildListItemChildText,
    DocumentConversationChildChildListItemChildToolCall,
    DocumentConversationChildChildListItemChildToolResult,
    DocumentConversationChildChildListItemChildTraceMessage,
    object,
]


class DocumentConversationChildChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentConversationChildChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentConversationChildChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildParagraphChild: TypeAlias = Union[
    DocumentConversationChildChildParagraphChildBlob,
    DocumentConversationChildChildParagraphChildCode,
    DocumentConversationChildChildParagraphChildComment,
    DocumentConversationChildChildParagraphChildDivider,
    DocumentConversationChildChildParagraphChildImage,
    DocumentConversationChildChildParagraphChildLink,
    DocumentConversationChildChildParagraphChildLineBreak,
    DocumentConversationChildChildParagraphChildText,
    DocumentConversationChildChildParagraphChildToolCall,
    DocumentConversationChildChildParagraphChildToolResult,
    DocumentConversationChildChildParagraphChildTraceMessage,
    object,
]


class DocumentConversationChildChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentConversationChildChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentConversationChildChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildQuoteChild: TypeAlias = Union[
    DocumentConversationChildChildQuoteChildBlob,
    DocumentConversationChildChildQuoteChildCode,
    DocumentConversationChildChildQuoteChildComment,
    DocumentConversationChildChildQuoteChildDivider,
    DocumentConversationChildChildQuoteChildImage,
    DocumentConversationChildChildQuoteChildLink,
    DocumentConversationChildChildQuoteChildLineBreak,
    DocumentConversationChildChildQuoteChildText,
    DocumentConversationChildChildQuoteChildToolCall,
    DocumentConversationChildChildQuoteChildToolResult,
    DocumentConversationChildChildQuoteChildTraceMessage,
    object,
]


class DocumentConversationChildChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentConversationChildChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentConversationChildChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentConversationChildChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildTableCellChild: TypeAlias = Union[
    DocumentConversationChildChildTableCellChildBlob,
    DocumentConversationChildChildTableCellChildCode,
    DocumentConversationChildChildTableCellChildComment,
    DocumentConversationChildChildTableCellChildDivider,
    DocumentConversationChildChildTableCellChildImage,
    DocumentConversationChildChildTableCellChildLink,
    DocumentConversationChildChildTableCellChildLineBreak,
    DocumentConversationChildChildTableCellChildText,
    DocumentConversationChildChildTableCellChildToolCall,
    DocumentConversationChildChildTableCellChildToolResult,
    DocumentConversationChildChildTableCellChildTraceMessage,
    object,
]


class DocumentConversationChildChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentConversationChildChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentConversationChildChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentConversationChildChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildChildToDoChild: TypeAlias = Union[
    DocumentConversationChildChildToDoChildBlob,
    DocumentConversationChildChildToDoChildCode,
    DocumentConversationChildChildToDoChildComment,
    DocumentConversationChildChildToDoChildDivider,
    DocumentConversationChildChildToDoChildImage,
    DocumentConversationChildChildToDoChildLink,
    DocumentConversationChildChildToDoChildLineBreak,
    DocumentConversationChildChildToDoChildText,
    DocumentConversationChildChildToDoChildToolCall,
    DocumentConversationChildChildToDoChildToolResult,
    DocumentConversationChildChildToDoChildTraceMessage,
    object,
]


class DocumentConversationChildChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentConversationChildChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentConversationChildChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentConversationChildChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentConversationChildChild: TypeAlias = Annotated[
    Union[
        DocumentConversationChildChildBlob,
        DocumentConversationChildChildCallout,
        DocumentConversationChildChildChunk,
        DocumentConversationChildChildCode,
        DocumentConversationChildChildComment,
        DocumentConversationChildChildDivider,
        DocumentConversationChildChildEquation,
        DocumentConversationChildChildFootnote,
        DocumentConversationChildChildHeading,
        DocumentConversationChildChildImage,
        DocumentConversationChildChildLink,
        DocumentConversationChildChildLineBreak,
        DocumentConversationChildChildList,
        DocumentConversationChildChildListItem,
        DocumentConversationChildChildParagraph,
        DocumentConversationChildChildQuote,
        DocumentConversationChildChildTable,
        DocumentConversationChildChildTableCell,
        DocumentConversationChildChildTableRow,
        DocumentConversationChildChildText,
        DocumentConversationChildChildToDo,
        DocumentConversationChildChildToolCall,
        DocumentConversationChildChildToolResult,
        DocumentConversationChildChildTraceMessage,
        DocumentConversationChildChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentConversationChildMentionedUserChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentConversationChildMentionedUserChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentConversationChildMentionedUserChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentConversationChildMentionedUserChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentConversationChildMentionedUserChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentConversationChildMentionedUserChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentConversationChildMentionedUserChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentConversationChildMentionedUserChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentConversationChildMentionedUserChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentConversationChildMentionedUserChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentConversationChildMentionedUserChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentConversationChildMentionedUserChild: TypeAlias = Union[
    DocumentConversationChildMentionedUserChildBlob,
    DocumentConversationChildMentionedUserChildCode,
    DocumentConversationChildMentionedUserChildComment,
    DocumentConversationChildMentionedUserChildDivider,
    DocumentConversationChildMentionedUserChildImage,
    DocumentConversationChildMentionedUserChildLink,
    DocumentConversationChildMentionedUserChildLineBreak,
    DocumentConversationChildMentionedUserChildText,
    DocumentConversationChildMentionedUserChildToolCall,
    DocumentConversationChildMentionedUserChildToolResult,
    DocumentConversationChildMentionedUserChildTraceMessage,
    object,
]


class DocumentConversationChildMentionedUser(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[List[str]] = None

    children: Optional[List[DocumentConversationChildMentionedUserChild]] = None

    company: Optional[str] = None

    company_ids: Optional[List[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[List[str]] = None

    email: Optional[str] = None

    emails: Optional[List[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


class DocumentConversationChild(BaseModel):
    date: datetime

    sender: DocumentConversationChildSender

    id: Optional[str] = None

    channel: Optional[str] = None
    """
    The channel or platform where the message was posted, if this Message is not
    explicitly part of a conversation
    """

    children: Optional[List[DocumentConversationChildChild]] = None

    external_id: Optional[str] = None
    """Provider message id (e.g. Slack ts, Gmail message id) — merge-dedup key"""

    is_self: Optional[bool] = None

    mentioned_users: Optional[List[DocumentConversationChildMentionedUser]] = None

    num_replies: Optional[int] = None

    replies: Optional[List[object]] = None
    """The replies or comments to the message"""

    text: Optional[str] = None

    thread_id: Optional[str] = None

    title: Optional[str] = None
    """The subject or title of the message"""

    type: Optional[Literal["message"]] = None

    updated_at: Optional[datetime] = None

    upvotes: Optional[int] = None
    """The number of upvotes, likes, or reactions on the message"""


class DocumentConversation(BaseModel):
    id: Optional[str] = None

    channel: Optional[str] = None

    children: Optional[List[DocumentConversationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["conversation"]] = None


class DocumentTraceChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentTraceChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTraceChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


DocumentTraceChild: TypeAlias = Annotated[
    Union[DocumentTraceChildTraceMessage, DocumentTraceChildToolCall, DocumentTraceChildToolResult],
    PropertyInfo(discriminator="type"),
]


class DocumentTrace(BaseModel):
    """An agent trace/transcript containing a sequence of steps.

    Steps can be TraceMessage (user/assistant messages or thinking),
    ToolCall (function calls), or ToolResult (tool responses).
    """

    id: Optional[str] = None

    children: Optional[List[DocumentTraceChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["trace"]] = None


class DocumentTranscriptChild(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


class DocumentTranscriptParticipantChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentTranscriptParticipantChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentTranscriptParticipantChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentTranscriptParticipantChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentTranscriptParticipantChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentTranscriptParticipantChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentTranscriptParticipantChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentTranscriptParticipantChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentTranscriptParticipantChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentTranscriptParticipantChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentTranscriptParticipantChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentTranscriptParticipantChild: TypeAlias = Union[
    DocumentTranscriptParticipantChildBlob,
    DocumentTranscriptParticipantChildCode,
    DocumentTranscriptParticipantChildComment,
    DocumentTranscriptParticipantChildDivider,
    DocumentTranscriptParticipantChildImage,
    DocumentTranscriptParticipantChildLink,
    DocumentTranscriptParticipantChildLineBreak,
    DocumentTranscriptParticipantChildText,
    DocumentTranscriptParticipantChildToolCall,
    DocumentTranscriptParticipantChildToolResult,
    DocumentTranscriptParticipantChildTraceMessage,
    object,
]


class DocumentTranscriptParticipant(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[List[str]] = None

    children: Optional[List[DocumentTranscriptParticipantChild]] = None

    company: Optional[str] = None

    company_ids: Optional[List[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[List[str]] = None

    email: Optional[str] = None

    emails: Optional[List[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


class DocumentTranscript(BaseModel):
    """
    A time-anchored, speaker-attributed transcript — meetings, calls
    (ENG-2476/D10; mirrors the Trace+TraceStep precedent).

    Utterance timestamps are relative offsets from `started_at`, which is the
    absolute wall-clock anchor.
    """

    id: Optional[str] = None

    children: Optional[List[DocumentTranscriptChild]] = None

    ended_at: Optional[datetime] = None

    participants: Optional[List[DocumentTranscriptParticipant]] = None

    started_at: Optional[datetime] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["transcript"]] = None


class DocumentCompanyChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildCalloutChild: TypeAlias = Union[
    DocumentCompanyChildCalloutChildBlob,
    DocumentCompanyChildCalloutChildCode,
    DocumentCompanyChildCalloutChildComment,
    DocumentCompanyChildCalloutChildDivider,
    DocumentCompanyChildCalloutChildImage,
    DocumentCompanyChildCalloutChildLink,
    DocumentCompanyChildCalloutChildLineBreak,
    DocumentCompanyChildCalloutChildText,
    DocumentCompanyChildCalloutChildToolCall,
    DocumentCompanyChildCalloutChildToolResult,
    DocumentCompanyChildCalloutChildTraceMessage,
    object,
]


class DocumentCompanyChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentCompanyChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentCompanyChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildChunkChild: TypeAlias = Union[
    DocumentCompanyChildChunkChildBlob,
    DocumentCompanyChildChunkChildCode,
    DocumentCompanyChildChunkChildComment,
    DocumentCompanyChildChunkChildDivider,
    DocumentCompanyChildChunkChildImage,
    DocumentCompanyChildChunkChildLink,
    DocumentCompanyChildChunkChildLineBreak,
    DocumentCompanyChildChunkChildText,
    DocumentCompanyChildChunkChildToolCall,
    DocumentCompanyChildChunkChildToolResult,
    DocumentCompanyChildChunkChildTraceMessage,
    object,
]


class DocumentCompanyChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentCompanyChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentCompanyChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildEquationChild: TypeAlias = Union[
    DocumentCompanyChildEquationChildBlob,
    DocumentCompanyChildEquationChildCode,
    DocumentCompanyChildEquationChildComment,
    DocumentCompanyChildEquationChildDivider,
    DocumentCompanyChildEquationChildImage,
    DocumentCompanyChildEquationChildLink,
    DocumentCompanyChildEquationChildLineBreak,
    DocumentCompanyChildEquationChildText,
    DocumentCompanyChildEquationChildToolCall,
    DocumentCompanyChildEquationChildToolResult,
    DocumentCompanyChildEquationChildTraceMessage,
    object,
]


class DocumentCompanyChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentCompanyChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentCompanyChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildFootnoteChild: TypeAlias = Union[
    DocumentCompanyChildFootnoteChildBlob,
    DocumentCompanyChildFootnoteChildCode,
    DocumentCompanyChildFootnoteChildComment,
    DocumentCompanyChildFootnoteChildDivider,
    DocumentCompanyChildFootnoteChildImage,
    DocumentCompanyChildFootnoteChildLink,
    DocumentCompanyChildFootnoteChildLineBreak,
    DocumentCompanyChildFootnoteChildText,
    DocumentCompanyChildFootnoteChildToolCall,
    DocumentCompanyChildFootnoteChildToolResult,
    DocumentCompanyChildFootnoteChildTraceMessage,
    object,
]


class DocumentCompanyChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentCompanyChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentCompanyChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildHeadingChild: TypeAlias = Union[
    DocumentCompanyChildHeadingChildBlob,
    DocumentCompanyChildHeadingChildCode,
    DocumentCompanyChildHeadingChildComment,
    DocumentCompanyChildHeadingChildDivider,
    DocumentCompanyChildHeadingChildImage,
    DocumentCompanyChildHeadingChildLink,
    DocumentCompanyChildHeadingChildLineBreak,
    DocumentCompanyChildHeadingChildText,
    DocumentCompanyChildHeadingChildToolCall,
    DocumentCompanyChildHeadingChildToolResult,
    DocumentCompanyChildHeadingChildTraceMessage,
    object,
]


class DocumentCompanyChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentCompanyChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentCompanyChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentCompanyChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildListItemChild: TypeAlias = Union[
    DocumentCompanyChildListItemChildBlob,
    DocumentCompanyChildListItemChildCode,
    DocumentCompanyChildListItemChildComment,
    DocumentCompanyChildListItemChildDivider,
    DocumentCompanyChildListItemChildImage,
    DocumentCompanyChildListItemChildLink,
    DocumentCompanyChildListItemChildLineBreak,
    DocumentCompanyChildListItemChildText,
    DocumentCompanyChildListItemChildToolCall,
    DocumentCompanyChildListItemChildToolResult,
    DocumentCompanyChildListItemChildTraceMessage,
    object,
]


class DocumentCompanyChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentCompanyChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentCompanyChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildParagraphChild: TypeAlias = Union[
    DocumentCompanyChildParagraphChildBlob,
    DocumentCompanyChildParagraphChildCode,
    DocumentCompanyChildParagraphChildComment,
    DocumentCompanyChildParagraphChildDivider,
    DocumentCompanyChildParagraphChildImage,
    DocumentCompanyChildParagraphChildLink,
    DocumentCompanyChildParagraphChildLineBreak,
    DocumentCompanyChildParagraphChildText,
    DocumentCompanyChildParagraphChildToolCall,
    DocumentCompanyChildParagraphChildToolResult,
    DocumentCompanyChildParagraphChildTraceMessage,
    object,
]


class DocumentCompanyChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentCompanyChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentCompanyChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildQuoteChild: TypeAlias = Union[
    DocumentCompanyChildQuoteChildBlob,
    DocumentCompanyChildQuoteChildCode,
    DocumentCompanyChildQuoteChildComment,
    DocumentCompanyChildQuoteChildDivider,
    DocumentCompanyChildQuoteChildImage,
    DocumentCompanyChildQuoteChildLink,
    DocumentCompanyChildQuoteChildLineBreak,
    DocumentCompanyChildQuoteChildText,
    DocumentCompanyChildQuoteChildToolCall,
    DocumentCompanyChildQuoteChildToolResult,
    DocumentCompanyChildQuoteChildTraceMessage,
    object,
]


class DocumentCompanyChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentCompanyChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentCompanyChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentCompanyChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildTableCellChild: TypeAlias = Union[
    DocumentCompanyChildTableCellChildBlob,
    DocumentCompanyChildTableCellChildCode,
    DocumentCompanyChildTableCellChildComment,
    DocumentCompanyChildTableCellChildDivider,
    DocumentCompanyChildTableCellChildImage,
    DocumentCompanyChildTableCellChildLink,
    DocumentCompanyChildTableCellChildLineBreak,
    DocumentCompanyChildTableCellChildText,
    DocumentCompanyChildTableCellChildToolCall,
    DocumentCompanyChildTableCellChildToolResult,
    DocumentCompanyChildTableCellChildTraceMessage,
    object,
]


class DocumentCompanyChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentCompanyChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentCompanyChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentCompanyChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentCompanyChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentCompanyChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentCompanyChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentCompanyChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentCompanyChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentCompanyChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentCompanyChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentCompanyChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentCompanyChildToDoChild: TypeAlias = Union[
    DocumentCompanyChildToDoChildBlob,
    DocumentCompanyChildToDoChildCode,
    DocumentCompanyChildToDoChildComment,
    DocumentCompanyChildToDoChildDivider,
    DocumentCompanyChildToDoChildImage,
    DocumentCompanyChildToDoChildLink,
    DocumentCompanyChildToDoChildLineBreak,
    DocumentCompanyChildToDoChildText,
    DocumentCompanyChildToDoChildToolCall,
    DocumentCompanyChildToDoChildToolResult,
    DocumentCompanyChildToDoChildTraceMessage,
    object,
]


class DocumentCompanyChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentCompanyChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentCompanyChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentCompanyChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentCompanyChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentCompanyChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentCompanyChild: TypeAlias = Annotated[
    Union[
        DocumentCompanyChildBlob,
        DocumentCompanyChildCallout,
        DocumentCompanyChildChunk,
        DocumentCompanyChildCode,
        DocumentCompanyChildComment,
        DocumentCompanyChildDivider,
        DocumentCompanyChildEquation,
        DocumentCompanyChildFootnote,
        DocumentCompanyChildHeading,
        DocumentCompanyChildImage,
        DocumentCompanyChildLink,
        DocumentCompanyChildLineBreak,
        DocumentCompanyChildList,
        DocumentCompanyChildListItem,
        DocumentCompanyChildParagraph,
        DocumentCompanyChildQuote,
        DocumentCompanyChildTable,
        DocumentCompanyChildTableCell,
        DocumentCompanyChildTableRow,
        DocumentCompanyChildText,
        DocumentCompanyChildToDo,
        DocumentCompanyChildToolCall,
        DocumentCompanyChildToolResult,
        DocumentCompanyChildTraceMessage,
        DocumentCompanyChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentCompany(BaseModel):
    """A CRM company/account record (ENG-2476/D10)."""

    id: Optional[str] = None

    address: Optional[str] = None

    children: Optional[List[DocumentCompanyChild]] = None

    contact_ids: Optional[List[str]] = None

    deal_ids: Optional[List[str]] = None

    description: Optional[str] = None

    emails: Optional[List[str]] = None

    employees: Optional[int] = None

    image_url: Optional[str] = None

    industry: Optional[str] = None

    is_active: Optional[bool] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    timezone: Optional[str] = None

    type: Optional[Literal["company"]] = None

    websites: Optional[List[str]] = None


class DocumentDealChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildCalloutChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildCalloutChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildCalloutChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildCalloutChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildCalloutChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildCalloutChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildCalloutChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildCalloutChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildCalloutChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildCalloutChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildCalloutChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildCalloutChild: TypeAlias = Union[
    DocumentDealChildCalloutChildBlob,
    DocumentDealChildCalloutChildCode,
    DocumentDealChildCalloutChildComment,
    DocumentDealChildCalloutChildDivider,
    DocumentDealChildCalloutChildImage,
    DocumentDealChildCalloutChildLink,
    DocumentDealChildCalloutChildLineBreak,
    DocumentDealChildCalloutChildText,
    DocumentDealChildCalloutChildToolCall,
    DocumentDealChildCalloutChildToolResult,
    DocumentDealChildCalloutChildTraceMessage,
    object,
]


class DocumentDealChildCallout(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDealChildCalloutChild]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["callout"]] = None


class DocumentDealChildChunkChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildChunkChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildChunkChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildChunkChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildChunkChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildChunkChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildChunkChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildChunkChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildChunkChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildChunkChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildChunkChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildChunkChild: TypeAlias = Union[
    DocumentDealChildChunkChildBlob,
    DocumentDealChildChunkChildCode,
    DocumentDealChildChunkChildComment,
    DocumentDealChildChunkChildDivider,
    DocumentDealChildChunkChildImage,
    DocumentDealChildChunkChildLink,
    DocumentDealChildChunkChildLineBreak,
    DocumentDealChildChunkChildText,
    DocumentDealChildChunkChildToolCall,
    DocumentDealChildChunkChildToolResult,
    DocumentDealChildChunkChildTraceMessage,
    object,
]


class DocumentDealChildChunk(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDealChildChunkChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["chunk"]] = None


class DocumentDealChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildEquationChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildEquationChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildEquationChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildEquationChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildEquationChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildEquationChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildEquationChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildEquationChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildEquationChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildEquationChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildEquationChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildEquationChild: TypeAlias = Union[
    DocumentDealChildEquationChildBlob,
    DocumentDealChildEquationChildCode,
    DocumentDealChildEquationChildComment,
    DocumentDealChildEquationChildDivider,
    DocumentDealChildEquationChildImage,
    DocumentDealChildEquationChildLink,
    DocumentDealChildEquationChildLineBreak,
    DocumentDealChildEquationChildText,
    DocumentDealChildEquationChildToolCall,
    DocumentDealChildEquationChildToolResult,
    DocumentDealChildEquationChildTraceMessage,
    object,
]


class DocumentDealChildEquation(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDealChildEquationChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["equation"]] = None


class DocumentDealChildFootnoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildFootnoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildFootnoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildFootnoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildFootnoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildFootnoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildFootnoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildFootnoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildFootnoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildFootnoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildFootnoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildFootnoteChild: TypeAlias = Union[
    DocumentDealChildFootnoteChildBlob,
    DocumentDealChildFootnoteChildCode,
    DocumentDealChildFootnoteChildComment,
    DocumentDealChildFootnoteChildDivider,
    DocumentDealChildFootnoteChildImage,
    DocumentDealChildFootnoteChildLink,
    DocumentDealChildFootnoteChildLineBreak,
    DocumentDealChildFootnoteChildText,
    DocumentDealChildFootnoteChildToolCall,
    DocumentDealChildFootnoteChildToolResult,
    DocumentDealChildFootnoteChildTraceMessage,
    object,
]


class DocumentDealChildFootnote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDealChildFootnoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["footnote"]] = None


class DocumentDealChildHeadingChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildHeadingChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildHeadingChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildHeadingChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildHeadingChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildHeadingChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildHeadingChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildHeadingChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildHeadingChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildHeadingChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildHeadingChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildHeadingChild: TypeAlias = Union[
    DocumentDealChildHeadingChildBlob,
    DocumentDealChildHeadingChildCode,
    DocumentDealChildHeadingChildComment,
    DocumentDealChildHeadingChildDivider,
    DocumentDealChildHeadingChildImage,
    DocumentDealChildHeadingChildLink,
    DocumentDealChildHeadingChildLineBreak,
    DocumentDealChildHeadingChildText,
    DocumentDealChildHeadingChildToolCall,
    DocumentDealChildHeadingChildToolResult,
    DocumentDealChildHeadingChildTraceMessage,
    object,
]


class DocumentDealChildHeading(BaseModel):
    level: int

    id: Optional[str] = None

    children: Optional[List[DocumentDealChildHeadingChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["heading"]] = None


class DocumentDealChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildList(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    ordered: Optional[bool] = None

    text: Optional[str] = None

    type: Optional[Literal["list"]] = None


class DocumentDealChildListItemChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildListItemChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildListItemChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildListItemChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildListItemChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildListItemChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildListItemChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildListItemChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildListItemChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildListItemChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildListItemChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildListItemChild: TypeAlias = Union[
    DocumentDealChildListItemChildBlob,
    DocumentDealChildListItemChildCode,
    DocumentDealChildListItemChildComment,
    DocumentDealChildListItemChildDivider,
    DocumentDealChildListItemChildImage,
    DocumentDealChildListItemChildLink,
    DocumentDealChildListItemChildLineBreak,
    DocumentDealChildListItemChildText,
    DocumentDealChildListItemChildToolCall,
    DocumentDealChildListItemChildToolResult,
    DocumentDealChildListItemChildTraceMessage,
    object,
]


class DocumentDealChildListItem(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDealChildListItemChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["list_item"]] = None


class DocumentDealChildParagraphChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildParagraphChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildParagraphChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildParagraphChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildParagraphChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildParagraphChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildParagraphChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildParagraphChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildParagraphChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildParagraphChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildParagraphChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildParagraphChild: TypeAlias = Union[
    DocumentDealChildParagraphChildBlob,
    DocumentDealChildParagraphChildCode,
    DocumentDealChildParagraphChildComment,
    DocumentDealChildParagraphChildDivider,
    DocumentDealChildParagraphChildImage,
    DocumentDealChildParagraphChildLink,
    DocumentDealChildParagraphChildLineBreak,
    DocumentDealChildParagraphChildText,
    DocumentDealChildParagraphChildToolCall,
    DocumentDealChildParagraphChildToolResult,
    DocumentDealChildParagraphChildTraceMessage,
    object,
]


class DocumentDealChildParagraph(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDealChildParagraphChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["paragraph"]] = None


class DocumentDealChildQuoteChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildQuoteChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildQuoteChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildQuoteChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildQuoteChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildQuoteChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildQuoteChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildQuoteChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildQuoteChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildQuoteChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildQuoteChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildQuoteChild: TypeAlias = Union[
    DocumentDealChildQuoteChildBlob,
    DocumentDealChildQuoteChildCode,
    DocumentDealChildQuoteChildComment,
    DocumentDealChildQuoteChildDivider,
    DocumentDealChildQuoteChildImage,
    DocumentDealChildQuoteChildLink,
    DocumentDealChildQuoteChildLineBreak,
    DocumentDealChildQuoteChildText,
    DocumentDealChildQuoteChildToolCall,
    DocumentDealChildQuoteChildToolResult,
    DocumentDealChildQuoteChildTraceMessage,
    object,
]


class DocumentDealChildQuote(BaseModel):
    id: Optional[str] = None

    children: Optional[List[DocumentDealChildQuoteChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["quote"]] = None


class DocumentDealChildTable(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


class DocumentDealChildTableCellChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildTableCellChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildTableCellChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildTableCellChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildTableCellChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildTableCellChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildTableCellChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildTableCellChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildTableCellChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildTableCellChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildTableCellChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildTableCellChild: TypeAlias = Union[
    DocumentDealChildTableCellChildBlob,
    DocumentDealChildTableCellChildCode,
    DocumentDealChildTableCellChildComment,
    DocumentDealChildTableCellChildDivider,
    DocumentDealChildTableCellChildImage,
    DocumentDealChildTableCellChildLink,
    DocumentDealChildTableCellChildLineBreak,
    DocumentDealChildTableCellChildText,
    DocumentDealChildTableCellChildToolCall,
    DocumentDealChildTableCellChildToolResult,
    DocumentDealChildTableCellChildTraceMessage,
    object,
]


class DocumentDealChildTableCell(BaseModel):
    id: Optional[str] = None

    align: Optional[Literal["left", "center", "right"]] = None

    children: Optional[List[DocumentDealChildTableCellChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_cell"]] = None


class DocumentDealChildTableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List[object]] = None

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


class DocumentDealChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildToDoChildBlob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    type: Optional[Literal["blob"]] = None


class DocumentDealChildToDoChildCode(BaseModel):
    text: str

    id: Optional[str] = None

    language: Optional[str] = None

    type: Optional[Literal["code"]] = None


class DocumentDealChildToDoChildComment(BaseModel):
    text: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["comment"]] = None


class DocumentDealChildToDoChildDivider(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class DocumentDealChildToDoChildImage(BaseModel):
    src: str

    text: str

    id: Optional[str] = None

    type: Optional[Literal["image"]] = None


class DocumentDealChildToDoChildLink(BaseModel):
    text: str

    url: str

    id: Optional[str] = None

    type: Optional[Literal["link"]] = None


class DocumentDealChildToDoChildLineBreak(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["line_break"]] = None


class DocumentDealChildToDoChildText(BaseModel):
    text: str

    id: Optional[str] = None

    marks: Optional[List[Literal["bold", "italic", "underline", "strikethrough", "code", "math"]]] = None

    type: Optional[Literal["text"]] = None


class DocumentDealChildToDoChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildToDoChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildToDoChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


DocumentDealChildToDoChild: TypeAlias = Union[
    DocumentDealChildToDoChildBlob,
    DocumentDealChildToDoChildCode,
    DocumentDealChildToDoChildComment,
    DocumentDealChildToDoChildDivider,
    DocumentDealChildToDoChildImage,
    DocumentDealChildToDoChildLink,
    DocumentDealChildToDoChildLineBreak,
    DocumentDealChildToDoChildText,
    DocumentDealChildToDoChildToolCall,
    DocumentDealChildToDoChildToolResult,
    DocumentDealChildToDoChildTraceMessage,
    object,
]


class DocumentDealChildToDo(BaseModel):
    id: Optional[str] = None

    checked: Optional[bool] = None

    children: Optional[List[DocumentDealChildToDoChild]] = None

    text: Optional[str] = None

    type: Optional[Literal["todo"]] = None


class DocumentDealChildToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    type: Optional[Literal["tool_call"]] = None


class DocumentDealChildToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    type: Optional[Literal["tool_result"]] = None


class DocumentDealChildTraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None


class DocumentDealChildUtterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    speaker: Optional[object] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


DocumentDealChild: TypeAlias = Annotated[
    Union[
        DocumentDealChildBlob,
        DocumentDealChildCallout,
        DocumentDealChildChunk,
        DocumentDealChildCode,
        DocumentDealChildComment,
        DocumentDealChildDivider,
        DocumentDealChildEquation,
        DocumentDealChildFootnote,
        DocumentDealChildHeading,
        DocumentDealChildImage,
        DocumentDealChildLink,
        DocumentDealChildLineBreak,
        DocumentDealChildList,
        DocumentDealChildListItem,
        DocumentDealChildParagraph,
        DocumentDealChildQuote,
        DocumentDealChildTable,
        DocumentDealChildTableCell,
        DocumentDealChildTableRow,
        DocumentDealChildText,
        DocumentDealChildToDo,
        DocumentDealChildToolCall,
        DocumentDealChildToolResult,
        DocumentDealChildTraceMessage,
        DocumentDealChildUtterance,
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentDeal(BaseModel):
    """A CRM deal/opportunity record (ENG-2476/D10)."""

    id: Optional[str] = None

    amount: Optional[float] = None

    children: Optional[List[DocumentDealChild]] = None

    closed_at: Optional[datetime] = None

    company_ids: Optional[List[str]] = None

    contact_ids: Optional[List[str]] = None

    currency: Optional[str] = None

    deal_source: Optional[str] = None

    lost_reason: Optional[str] = None

    name: Optional[str] = None

    pipeline: Optional[str] = None

    probability: Optional[float] = None

    stage: Optional[str] = None

    tags: Optional[List[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["deal"]] = None

    won_reason: Optional[str] = None


Document: TypeAlias = Annotated[
    Union[
        DocumentDocument,
        DocumentWebsite,
        DocumentTask,
        DocumentPerson,
        DocumentMessage,
        DocumentEvent,
        DocumentFile,
        DocumentConversation,
        DocumentTrace,
        DocumentTranscript,
        DocumentCompany,
        DocumentDeal,
    ],
    PropertyInfo(discriminator="type"),
]


class MemoryGetResponse(BaseModel):
    """A document-shaped API response carrying the hyperdoc tree (ENG-2479/D12)."""

    document: Document
    """The full hyperdoc tree.

    Switch on `type` for the document frame and recurse `children` for the body —
    see the `<Hyperdoc />` renderer.
    """

    resource_id: str

    source: Literal[
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "box",
        "dropbox",
        "github",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
        "microsoft_teams",
        "gmail_actions",
        "granola",
        "fathom",
        "fireflies",
        "linear",
        "hubspot",
        "salesforce",
        "coda",
        "lightfield",
    ]

    type: str
    """Hyperdoc document type discriminator (document, message, file, event, ...)."""

    collection: Optional[str] = None
    """The document's collection, if any."""

    document_date: Optional[datetime] = None
    """The document's own date (e.g. email sent date, event date)."""

    ingested_at: Optional[datetime] = None
    """When Hyperspell first indexed the document."""

    last_modified_at: Optional[datetime] = None
    """When the source document was last modified."""

    metadata: Optional[Dict[str, object]] = None
    """Filterable custom metadata attached to the document."""

    status: Optional[Literal["pending", "processing", "completed", "failed", "pending_review", "skipped"]] = None
    """Indexing status of the document."""

    title: Optional[str] = None
    """Human-readable document title."""
